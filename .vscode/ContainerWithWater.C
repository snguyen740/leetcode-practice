int maxArea(int* height, int heightSize){
    int water = 0, *i = height, *j = i + heightSize - 1;
    while (i < j){
        int h = *i < *j ? *i : *j;
        int w = (j-i) * h;
        if (w > water) water = w;
        while (*i <= h && i < j) i++;
        while (*j <= h && i < j) j--;
    }
    return water;
}

// Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of the line i is at (i, ai) and (i, 0). Find two lines, which, together with the x-axis forms a container, such that the container contains the most water.