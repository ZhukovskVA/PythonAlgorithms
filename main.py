def square_root_bisection(number, tolerance = 1e-7, max_iter = 100):
    if number < 0:
        raise ValueError('Square root of negative number is not defined in real numbers')
    elif number == 0 or number == 1:
        print(f"The square root of {number} is {number}")
        return number
    else:
        low = 0
        high = max(1, number)
        iteration = 0
        while iteration < max_iter:
            mid = (low + high) / 2
            square_mid = mid ** 2
            if (high - low) < tolerance:
                root = mid
                print(f"The square root of {number} is approximately {root}")
                return root
            elif number < square_mid:
                high = mid
            else:
                low = mid
            iteration += 1
            if iteration == max_iter:
                print(f"Failed to converge within {max_iter} iterations")
                return None

