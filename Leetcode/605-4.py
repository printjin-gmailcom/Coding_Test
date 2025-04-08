def canPlaceFlowers(flowerbed: list[int], n: int) -> bool:
    available_spots = 0
    flowerbed = [0] + flowerbed + [0]
    
    for i in range(1, len(flowerbed) - 1):
        if flowerbed[i - 1] == flowerbed[i] == flowerbed[i + 1] == 0:
            flowerbed[i] = 1
            available_spots += 1
            
        if available_spots >= n:
            return True
            
    return available_spots >= n
