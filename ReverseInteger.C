int reverse(int x){
    int r = 0;
    long sum = 0;
    while (x != 0)
    {
        r = x%10;
        sum = sum*10 + r;
        x = x/10;
        if(sum > INT32_MAX || sum < INT32_MIN)
            return 0;
    }
    return sum;
}

// Given a 32-bit signed integer, reverse digits of an integer.