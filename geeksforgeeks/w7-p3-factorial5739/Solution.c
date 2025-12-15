// Function to calculate factorial of a number.
int factorial(int n) {
    if(n==1||0) {
        return n;
    }
    return n*factorial(n-1);
}
