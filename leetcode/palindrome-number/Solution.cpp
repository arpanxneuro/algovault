class Solution
{
public:
    bool isPalindrome(int x)
    {
        if (x < 0)
            return false;

        long long rev = 0, orig = x;
        while (x != 0)
        {
            rev = rev * 10 + x % 10;
            x /= 10;
        }
        return rev == orig;
    }
};
