import asyncio
from inspect import Signature, Parameter
import random
from typing import Any, List, Union, Dict
from collections.abc import Callable

from treelang.ai.provider import ToolProvider


class TreeNode:
    """
    Represents a node in the abstract syntax tree (AST).

    Attributes:
        type (str): The type of the AST node.

    Methods:
        eval(ToolProvider): Evaluates the node using the provided ToolProvider.
    """

    def __init__(self, node_type: str) -> None:
        self.type = node_type

    async def eval(self, provider: ToolProvider) -> Any:
        raise NotImplementedError()


class TreeProgram(TreeNode):
    """
    Represents a program in the abstract syntax tree (AST).

    Attributes:
        body (List[TreeNode]): The list of statements in the program.
        name str: optional name for this program.
        description str: optional description for this program.

    Methods:
        eval(ToolProvider): Evaluates the program by evaluating each statement in the body.
    """

    def __init__(
        self, body: List[TreeNode], name: str = None, description: str = None
    ) -> None:
        super().__init__("program")
        self.body = body
        self.name = name
        self.description = description

    async def eval(self, provider: ToolProvider) -> Any:
        result = await asyncio.gather(*[node.eval(provider) for node in self.body])
        return result[0] if len(result) == 1 else result


class TreeFunction(TreeNode):
    """
    Represents a function in the abstract syntax tree (AST).

    Attributes:
        name (str): The name of the function.
        params (List[str]): The list of parameters of the function.

    Methods:
        eval(ToolProvider): Evaluates the function by calling the underlying tool with the provided parameters.
    """

    def __init__(self, name: str, params: List[TreeNode]) -> None:
        super().__init__("function")
        self.name = name
        self.params = params

    async def eval(self, provider: ToolProvider) -> Any:
        tool = await provider.get_tool_definition(self.name)

        if not tool:
            raise ValueError(f"Tool {self.name} is not available")

        tool_properties = tool["properties"].keys()

        # evaluate each parameter in order
        results = await asyncio.gather(*[param.eval(provider) for param in self.params])
        # create a dictionary of parameter names and values
        params = dict(zip(tool_properties, results))
        # invoke the underlying tool
        output = await provider.call_tool(self.name, params)

        return output.content


class TreeValue(TreeNode):
    """
    Represents a value in the abstract syntax tree (AST).

    Attributes:
        value (Any): The value of the node.

    Methods:
        eval(ToolProvider): Returns the value of the node.
    """

    def __init__(self, name: str, value: Any) -> None:
        super().__init__("value")
        self.name = name
        self.value = value

    async def eval(self, provider: ToolProvider) -> Any:
        return self.value


class TreeConditional(TreeNode):
    """
    Represents a conditional statement in the AST.

    Attributes:
        condition (TreeNode): The condition to evaluate.
        true_branch (TreeNode): The branch to execute if the condition is true.
        false_branch (TreeNode): The branch to execute if the condition is false.

    Methods:
        eval(ToolProvider): Evaluates the condition and executes the appropriate branch.
    """

    def __init__(
        self, condition: TreeNode, true_branch: TreeNode, false_branch: TreeNode = None
    ) -> None:
        super().__init__("conditional")
        self.condition = condition
        self.true_branch = true_branch
        self.false_branch = false_branch

    async def eval(self, provider: ToolProvider) -> Any:
        condition_result = await self.condition.eval(provider)

        if condition_result:
            return await self.true_branch.eval(provider)
        elif self.false_branch:
            return await self.false_branch.eval(provider)

        return None


class TreeLambda(TreeNode):
    """
    Represents an anonymous (lambda) function.
    Attributes:
        params (List[str]): Parameter names.
        body (TreeFunction): The function body.
    """

    def __init__(self, params: List[str], body: TreeFunction):
        super().__init__("lambda")
        self.params = params
        self.body = body

    async def eval(self, provider: ToolProvider):
        # Returns a callable that can be invoked with arguments
        async def func(*args):
            # update this TreeFunction's argument values with
            # the provided arguments preserving the order. Note that
            # the number of arguments maybe less than or equal to
            # the number of parameters but not more.
            for i, param in enumerate(self.body.params):
                if i < len(args):
                    param.value = args[i]
                else:
                    # if there are not enough arguments, we leave the parameter value as is
                    break
            return await self.body.eval(provider)

        return func


class TreeMap(TreeNode):
    """
    Represents a map operation in the abstract syntax tree (AST).

    Attributes:
        function (TreeLambda): The function to apply to each item in the iterable.
        iterable (TreeNode): The iterable to map over. The iterable TreeNode should evaluate to a list.

    Methods:
        eval(ToolProvider): Applies the map function to each item in the iterable.
    """

    def __init__(self, function: TreeLambda, iterable: TreeNode):
        super().__init__("map")
        self.function = function
        self.iterable = iterable

    async def eval(self, provider: ToolProvider) -> Any:
        items = await self.iterable.eval(provider)

        if not isinstance(items, list):
            raise TypeError("Map expects an iterable (list) as input")

        func = await self.function.eval(provider)

        return [await func(item) for item in items]


class TreeFilter(TreeNode):
    """
    Represents a filter operation in the abstract syntax tree (AST).

    Attributes:
        function (TreeLambda): The function to apply to each item in the iterable. The function should return a boolean value.
        iterable (TreeNode): The iterable to filter. The iterable TreeNode should evaluate to a list.

    Methods:
        eval(ToolProvider): Applies the filter function to each item in the iterable.
    """

    def __init__(self, function: TreeLambda, iterable: TreeNode):
        super().__init__("filter")
        self.function = function
        self.iterable = iterable

    async def eval(self, provider: ToolProvider) -> Any:
        items = await self.iterable.eval(provider)

        if not isinstance(items, list):
            raise TypeError("Filter expects an iterable (list) as input")

        func = await self.function.eval(provider)

        return [item for item in items if await func(item)]


class TreeReduce(TreeNode):
    """
    Represents a reduce operation in the abstract syntax tree (AST).

    Attributes:
        function (TreeLambda): The function to apply to each item in the iterable. The function should take two arguments,
                               the accumulated value and the current item, and return a new accumulated value.
        iterable (TreeNode): The iterable to reduce. The iterable TreeNode should evaluate to a list.

    Methods:
        eval(ToolProvider): Applies the reduce function to each item in the iterable.
    """

    def __init__(self, function: TreeLambda, iterable: TreeNode):
        super().__init__("reduce")
        self.function = function
        self.iterable = iterable

    async def eval(self, provider: ToolProvider) -> Any:
        items = await self.iterable.eval(provider)

        if not isinstance(items, list):
            raise TypeError("Reduce expects an iterable (list) as input")

        func = await self.function.eval(provider)

        if not items:
            return None

        result = items[0]

        for item in items[1:]:
            result = await func(result, item)

        return result


class AST:
    """
    Represents an Abstract Syntax Tree (AST) for a very simple programming language.
    """

    @classmethod
    def parse(cls, ast: Union[Dict[str, Any], List[Dict[str, Any]]]) -> TreeNode:
        """
        Parses the given dictionary or list into a TreeNode.

        Args:
            ast (Union[Dict[str, Any], List[Dict[str, Any]]]): The AST dictionary or list of dictionaries to parse.

        Returns:
            TreeNode: The parsed TreeNode.

        Raises:
            ValueError: If the node type is unknown.
        """
        if isinstance(ast, List):
            return [cls.parse(node) for node in ast]
        node_type = ast.get("type")

        if node_type == "program":
            return TreeProgram(cls.parse(ast["body"]))
        if node_type == "function":
            return TreeFunction(ast["name"], cls.parse(ast["params"]))
        if node_type == "value":
            return TreeValue(ast["name"], ast["value"])
        if node_type == "conditional":
            return TreeConditional(
                cls.parse(ast["condition"]),
                cls.parse(ast["true_branch"]),
                cls.parse(ast.get("false_branch")),
            )
        if node_type == "lambda":
            return TreeLambda(
                ast["params"],
                TreeFunction(ast["body"]["name"], cls.parse(ast["body"]["params"])),
            )
        if node_type == "map":
            return TreeMap(
                TreeLambda(
                    ast["function"]["params"],
                    TreeFunction(
                        ast["function"]["body"]["name"],
                        cls.parse(ast["function"]["body"]["params"]),
                    ),
                ),
                cls.parse(ast["iterable"]),
            )
        if node_type == "filter":
            # if the body of the function is a conditional, we can
            # we can extract the condition and use it directly
            if ast["function"]["body"]["type"] == "conditional":
                ast["function"]["body"] = ast["function"]["body"]["condition"]
                return cls.parse(ast)

            return TreeFilter(
                TreeLambda(
                    ast["function"]["params"],
                    TreeFunction(
                        ast["function"]["body"]["name"],
                        cls.parse(ast["function"]["body"]["params"]),
                    ),
                ),
                cls.parse(ast["iterable"]),
            )
        if node_type == "reduce":
            return TreeReduce(
                TreeLambda(
                    ast["function"]["params"],
                    TreeFunction(
                        ast["function"]["body"]["name"],
                        cls.parse(ast["function"]["body"]["params"]),
                    ),
                ),
                cls.parse(ast["iterable"]),
            )

        raise ValueError(f"unknown node type: {node_type}")

    @classmethod
    async def eval(cls, ast: TreeNode, provider: ToolProvider) -> Any:
        """
        Evaluates the given AST.

        Args:
            ast TreeNode: The AST to evaluate.

        Returns:
            Any: The result of evaluating the AST.
        """
        return await ast.eval(provider)

    @classmethod
    def visit(cls, ast: TreeNode, op: Callable[[TreeNode], None]) -> None:
        """
        Performs a depth-first visit of the AST and applies the given operation to each node.

        Args:
            ast (TreeNode): The root node of the AST.
            op (Callable[[TreeNode], None]): The operation to apply to each node.

        Returns:
            None
        """
        op(ast)  # Apply the operation to the current node

        if isinstance(ast, TreeProgram):
            for statement in ast.body:
                cls.visit(
                    statement, op
                )  # Recursively visit each statement in the program

        if isinstance(ast, TreeConditional):
            cls.visit(ast.condition, op)
            cls.visit(ast.true_branch, op)  # Recursively visit the true branch
            if ast.false_branch:
                cls.visit(ast.false_branch, op)  # Recursively visit the false branch

        if isinstance(ast, TreeLambda):
            cls.visit(ast.body, op)

        if any(
            [
                isinstance(ast, node_type)
                for node_type in [TreeMap, TreeFilter, TreeReduce]
            ]
        ):
            cls.visit(ast.function, op)
            cls.visit(ast.iterable, op)

        elif isinstance(ast, TreeFunction):
            for param in ast.params:
                cls.visit(param, op)  # Recursively visit each parameter of the function

    @classmethod
    async def avisit(cls, ast: TreeNode, op: Callable[[TreeNode], None]) -> None:
        """
        Performs an asynchronous depth-first visit of the AST and applies the given operation to each node.

        Args:
            ast (TreeNode): The root node of the AST.
            op (Callable[[TreeNode], None]): The operation to apply to each node.

        Returns:
            None
        """
        if asyncio.iscoroutinefunction(op):
            await op(ast)  # Apply the asynchronous operation to the current node
        else:
            return cls.visit(ast, op)  # Fallback to synchronous visit

        if isinstance(ast, TreeProgram):
            for statement in ast.body:
                await cls.avisit(
                    statement, op
                )  # Recursively visit each statement in the program

        if isinstance(ast, TreeConditional):
            await cls.avisit(ast.condition, op)
            await cls.avisit(ast.true_branch, op)
            if ast.false_branch:
                await cls.avisit(ast.false_branch, op)

        if isinstance(ast, TreeLambda):
            await cls.avisit(ast.body, op)

        if any(
            [
                isinstance(ast, node_type)
                for node_type in [TreeMap, TreeFilter, TreeReduce]
            ]
        ):
            await cls.avisit(ast.function, op)
            await cls.avisit(ast.iterable, op)

        elif isinstance(ast, TreeFunction):
            for param in ast.params:
                await cls.avisit(
                    param, op
                )  # Recursively visit each parameter of the function

    @classmethod
    def repr(cls, ast: TreeNode) -> str:
        """
        Returns a string representation of the given TreeNode.

        Parameters:
        - cls (class): The class containing the `repr` method.
        - ast (TreeNode): The TreeNode to be represented.

        Returns:
        - str: The string representation of the TreeNode.

        Example:
        >>> ast = TreeProgram(body=[TreeFunction(name='foo', params=['x', 'y']), TreeValue(name='z', value=10)])
        >>> AST.repr(ast)
        "{foo_1: {x, y}, z_1: [10]}"
        """
        representation = ""
        name_counts = dict()

        def _f(node: TreeNode):
            nonlocal representation
            if isinstance(node, TreeProgram):
                representation = "{" + ", ".join(["%s"] * len(node.body)) + "}"
            if isinstance(node, TreeFunction):
                name = node.name
                if name not in name_counts:
                    name_counts[name] = 0
                name_counts[name] += 1
                args = "{" + ", ".join(["%s"] * len(node.params)) + "}"
                representation = representation.replace(
                    "%s", f'"{name}_{name_counts[name]}": {args}', 1
                )
            if isinstance(node, TreeValue):
                name = node.name
                value = node.value
                if type(value) is str:
                    value = f'"{value}"'
                if type(value) is bool:
                    value = str(value).lower()
                if type(value) is list:
                    value = (
                        "["
                        + ", ".join(
                            [f'"{v}"' if isinstance(v, str) else str(v) for v in value]
                        )
                        + "]"
                    )
                if isinstance(value, float) and value.is_integer():
                    value = int(value)
                representation = representation.replace("%s", f'"{name}": [{value}]', 1)
            if isinstance(node, TreeConditional):
                name = "conditional"

                if name not in name_counts:
                    name_counts[name] = 0

                name_counts[name] += 1
                num_operands = 3 if node.false_branch else 2
                args = "{" + ", ".join(["%s"] * num_operands) + "}"

                representation = representation.replace(
                    "%s",
                    f'"{name}_{name_counts[name]}": {args}',
                    1,
                )
            if isinstance(node, TreeLambda):
                name = "lambda"

                if name not in name_counts:
                    name_counts[name] = 0

                name_counts[name] += 1
                args = "{" + ", ".join(["%s"]) + "}"
                representation = representation.replace(
                    "%s", f'"{name}_{name_counts[name]}": {args}', 1
                )
            if isinstance(node, TreeMap):
                name = "map"

                if name not in name_counts:
                    name_counts[name] = 0

                name_counts[name] += 1
                args = "{" + ", ".join(["%s"] * 2) + "}"
                representation = representation.replace(
                    "%s", f'"{name}_{name_counts[name]}": {args}', 1
                )
            if isinstance(node, TreeFilter):
                name = "filter"

                if name not in name_counts:
                    name_counts[name] = 0

                name_counts[name] += 1
                args = "{" + ", ".join(["%s"] * 2) + "}"
                representation = representation.replace(
                    "%s", f'"{name}_{name_counts[name]}": {args}', 1
                )
            if isinstance(node, TreeReduce):
                name = "reduce"

                if name not in name_counts:
                    name_counts[name] = 0

                name_counts[name] += 1
                args = "{" + ", ".join(["%s"] * 2) + "}"
                representation = representation.replace(
                    "%s", f'"{name}_{name_counts[name]}": {args}', 1
                )

        cls.visit(ast, _f)

        return representation.replace("None", "")

    @staticmethod
    async def tool(ast: TreeNode, provider: ToolProvider) -> Callable[..., Any]:
        """
        Converts the given AST into a callable function that can be
        added as a tool to the MCP server.

        Args:
            ast (TreeNode): The AST to convert.

        Returns:
            AnyFunction: The callable function representation of the AST.
        """
        if not isinstance(ast, TreeProgram):
            raise ValueError("AST root must be a TreeProgram")

        tool_signature = None

        # map json types from tool definitions to python types
        types_map = {
            "string": str,
            "integer": int,
            "number": float,
            "boolean": bool,
            "array": list,
            "object": dict,
        }

        # the program must have a name and description
        if not ast.name:
            raise ValueError("AST program must have a name")
        if not ast.description:
            raise ValueError("AST program must have a description")

        # extract the programs' parameters from the tree
        param_objects = []

        # the arguments of the new tool are to be gathered from
        # the leaves of the tree
        def inject(
            param_objs: List[Parameter],
            props: List[Dict[str, Any]],
            arg_names: List[str],
        ) -> Callable[[TreeNode], None]:
            async def _f(node: TreeNode):
                # for now we do not support higher order functions here
                if any(isinstance(node, t) for t in [TreeLambda, TreeMap]):
                    raise ValueError(
                        "Higher order functions (lambdas, maps) are not yet supported in tool creation"
                    )
                if isinstance(node, TreeFunction):
                    other_dfn = await provider.get_tool_definition(node.name)
                    # let's get this function's parameters into the props stack
                    props.append(other_dfn["properties"])

                if isinstance(node, TreeValue):
                    # since this is a leaf node, we can add it to the parameters
                    # of the new tool
                    if node.name not in props[-1]:
                        # if we are here, we are are now processing
                        # a function node up the tree and we can
                        # pop the properties stack
                        props.pop()

                    properties = props[-1]
                    key = node.name
                    # be mindful of duplicate arguments names
                    if key in arg_names:
                        # we add a random suffix to the key
                        key = key + f"_{random.randint(1, 1000)}"
                        # rename the parameter in the properties dict
                        properties = {
                            key if k == node.name else k: v
                            for k, v in properties.items()
                        }
                        node.name = key
                    arg_names.append(key)
                    param_objs.append(
                        Parameter(
                            key,
                            Parameter.KEYWORD_ONLY,
                            annotation=types_map.get(
                                properties[node.name]["type"], Any
                            ),
                        )
                    )

            return _f

        await AST.avisit(ast, inject(param_objects, [], []))

        try:
            tool_signature = Signature(
                parameters=param_objects,
            )
        except ValueError as e:
            raise ValueError(f"Invalid function signature for {ast.name}") from e

        # convert the AST to a callable function
        async def wrapper(*args, **kwargs):
            try:
                # bind the arguments to our tool signature
                bound_args = tool_signature.bind(*args, **kwargs)
                # apply the default values if any
                bound_args.apply_defaults()
            except TypeError as e:
                raise TypeError(f"Argument binding failed for {ast.name}(): {e}") from e
            # evaluating this tool is equivalent to evaluating the AST
            # thus, we need to inject the arguments'values into the AST
            try:

                def inject(*vargs, **vwargs) -> Callable[[TreeNode], None]:
                    def _f(node: TreeNode) -> None:
                        if isinstance(node, TreeValue):
                            if vwargs and node.name in vwargs:
                                node.value = vwargs[node.name]
                            elif vargs:
                                node.value = vargs.pop()

                    return _f

                AST.visit(ast, inject(*bound_args.args, **bound_args.kwargs))
                # finally, evaluate the AST
                return await ast.eval(provider)
            except Exception as e:
                raise RuntimeError(f"Error executing {ast.name}(): {e}") from e

        # set the function's signature and metadata
        wrapper.__name__ = ast.name
        wrapper.__doc__ = ast.description
        wrapper.__signature__ = tool_signature

        return wrapper
