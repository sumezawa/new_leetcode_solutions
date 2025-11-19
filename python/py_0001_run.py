from py_0001 import solver

def main():
    submission = solver()
    args = [([2,7,11,15],9),
            ([3,2,4],6),
            ([3,3],6)]
    for item in args:
        ans = submission.two_sum(item[0], item[1])
        print(ans)

if __name__ == "__main__":
    main()





