class Solution:
    def hIndex(self, citations: List[int]) -> int:
        # numOfCitations = len(citations)
        # while numOfCitations > 0:
        #     count = 0
        #     for i in citations:
        #         if i >= numOfCitations:
        #             count += 1
        #         if count == numOfCitations:
        #             return count
        #     numOfCitations -= 1
        # return 0

        # In my 1st approach I took the full length of citations and then I iterated through the list and checked which
        # elements are greater than equal to the len of citations and if there is any then I was counting them how many
        # elements are such and then at last I was comparing the count with its len if it gets matched then I was
        # returning the count else I was decrimenting the length by 1 and then doing the same performance
        # at last if the list is blank or there is one or more element in the list which has the citations of 0
        # then the final citations would be 0 hence the default return type I made was 0
        


        # 2nd approach
        temp = {}
        for i in range(max(citations), min(citations) - 1, -1):
            temp[i] = 0

        for l in citations:
            if l in temp.keys():
                temp[l] += 1

        print(temp)
        newList = []     
        for key, value in temp.items():
            if key > len(citations):
                newList.extend([len(citations)] * value)
            else:
                newList.extend([key] * value)

        # The above 2 is for sorting algo , its a count sort where we take min and max of the list and then within that
        # window we perform comparision with the range of all numbers in that range which comes is there inside the list
        # we take a note of that and keep a count of that then we recreate a new array, it is not space friendly,
        # the 1st cmd is counting the elements and the 2nd cmd is for constructing a new list but here I did a little
        # twik where I added the max length number instead of any number that is greater than max length as we don't care
        # about the greater numbers exceeding the number of citations the scirntest has produced it basically has the
        # same meaning
        print(newList)
        for index,m in enumerate(newList):
            if (index + 1) < m:
                continue
            elif index + 1 > m:
                return index
            elif index + 1 == m:
                return index + 1 
        return 0


# [3,0,6,1,5]  [0,1,3,5,6]
# [6,5,3,1,0]


        # we will 1st sort the list by doing so we will be able to match the index + 1 with its values
        # Like [3,0,6,1,5] we will sort it but in a different way so as the total elements are 5 so we don't care if any
        # of the value is more than 5 coz that would essentially have the same meaning interms of H-index
        # hence what we will do we will create a new array and how we will create that is we will go from 0 to till the
        # length of the array and each time we will check how many that item is present, for eg: 0 is present how many
        # times if its present in our main array more than 0 times we will add to to our new array that many times
        # then move to 1 and do the same untill you reach to last element that is the length of the main array when you
        # will reach at that position you will check whether the current elemnt is present or not or is there any element
        # greater than the current element if yes then how many times those greater elements are present same times you
        # will put the last element as if any element is greater than the current last element that essentially menas 
        # it does have the same contribution as of last element
        # then after the sorting is done and we have your new array we will iterate through the array and we will start
        # from matching that whether the 1st element is greater than equal to index + 1 if yes then we move to next
        # and check the same untill we reach that the current element is equal to the index + 1 then we will stop there
        # and return that index / value
        # Sorting would take O(n)
        # iterating through new list would take O(n)
        # Total O(2n) , and as we don't consider constants hence it will be O(n)