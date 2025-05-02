function evaluatePostfix(instructions) {
    let stack = [];

    for (let item of instructions) {
        if (typeof item === "number") {
            stack.push(item);
        } else if (["+", "-", "*", "/"].includes(item)) {
            if (stack.length < 2) {
                console.log("Error: not enough operands!");
                return;
            }

            let b = stack.pop();
            let a = stack.pop();

            switch (item) {
                case "+":
                    stack.push(a + b);
                    break;
                case "-":
                    stack.push(a - b);
                    break;
                case "*":
                    stack.push(a * b);
                    break;
                case "/":
                    stack.push(a / b);
                    break;
            }
        }
    }

    if (stack.length === 1) {
        console.log(stack[0]);
    } else {
        console.log("Error: too many operands!");
    }
}
