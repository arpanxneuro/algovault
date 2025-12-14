class Solution
{
public:
    vector<string> divideString(string s, int k, char fill)
    {
        vector<string> myArr;
        int n = s.length();
        int remainder = n % k;
        if (remainder != 0)
        {
            int padCount = k - remainder;
            s.append(padCount, fill);
        }
        for (int i = 0; i < (int)s.length(); i += k)
        {
            myArr.push_back(s.substr(i, k));
        }

        return myArr;
    }
};
