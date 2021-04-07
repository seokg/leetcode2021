class Solution:
    # Runtime: 320 ms
    # Memory Usage: 19.4 MB
    def __init__(self, nums: List[int]):
        self.list = nums

    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        return self.list
        

    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        import random
        new_list = self.list.copy()
        for i in range(len(self.list)):
            index = random.randrange(0, len(self.list))
            new_list[i], new_list[index] = new_list[index], new_list[i]
        assert len(self.list) == len(new_list), "length error"
        return new_list
        