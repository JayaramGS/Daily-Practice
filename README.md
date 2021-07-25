# Daily-Practice
This Repository contains Python solutions for problems that I solved everyday. 

# Day 1 
# Detect_Capital.py
Given a string s, return the string after replacing every uppercase letter with the same lowercase letter.

Input Format
Hello

Constraints
1 <= s.length <= 100 s consists of printable ASCII characters.

Output Format
hello

# Number_of_Segments_in_a_String.py
You are given a string s, return the number of segments in the string.
A segment is defined to be a contiguous sequence of non-space characters.

Input Format
Hello, my name is John

Constraints
0 <= s.length <= 300 s consists of lower-case and upper-case English letters, digits or one of the following characters "!@#$%^&*()_+-=',.:". The only space character in s is ' '.

Output Format
5

# Detect_Capital.py
We define the usage of capitals in a word to be right when one of the following cases holds:
All letters in this word are capitals, like "USA". All letters in this word are not capitals, like "leetcode". Only the first letter in this word is capital, like "Google". Given a string word, return true if the usage of capitals in it is right.

Input Format
USA

Constraints
1 <= word.length <= 100 word consists of lowercase and uppercase English letters.

Output Format
true

# Day 2
# Obtain_the_domain_name_from_the_url.py

Obtain the domain name from the url

Input Format
The input will be a string. For Eg: 'https://www.youtube.com'

Constraints
none

Output Format
The Output format should be in string. For Eg: youtube.com

# To_make_a_full_url_from a_String.py

To make a full url from a given string

Input Format
The input will be as a string.

Constraints
none

Output Format
The output will be as a url format.

# Day 3
# Print_the_maximum_possible_integer.py

The program must accept an integer N as the input. The program must print the maximum possible Integer X which is less than N, but the sum of digits in X is greater than the sum of digits in N. If there is no such integer, the program must print the integer N as it is.

Input Format
35

Constraints
none

Output Format
29

# Print_the_missing_alphabets.py

The program must accept a string S containing only lower case alphabets as the input. The program must print the missing lower case alphabets in string S in alphabetical order as the output. Note: At least one lower case is always missing in the string S.

Input Format
The input must be in string which can include alphanumeric, number etc.

Constraints
None

Output Format
The output must be in string

# Day 4
# Height_Checker.py

A school is trying to take an annual photo of all the students. The students are asked to stand in a single file line in non-decreasing order by height. Let this ordering be represented by the integer array expected where expected[i] is the expected height of the ith student in line.
You are given an string with integer heights representing the current order that the students are standing in. Each heights[i] is the height of the ith student in line (0-indexed).
Return the number of indices where heights[i] != expected[i].

Input Format
The input format will be in string

Constraints
1 <= heights.length <= 100 1 <= heights[i] <= 100

Output Format
The output format will be in a integer

# Build_an_Array_With_Stack_Operations.py

Given an string targets separated with hyphen '-' with an integer n separated by '#'. In each iteration, you will read a number from string.
Build the string number values using the following operations:
Push: Read a new element from the beginning of the string number values, and push it in the array. Pop: delete the last element from the string. If the target value in the string is already built, stop reading more elements. Return the operations to build the target array. You are guaranteed that the answer is unique.

Input Format
The input format is string

Constraints
1 <= target.length <= 100 1 <= target[i] <= n 1 <= n <= 100 target is strictly increasing.

Output Format
The output format is array

# Day 5
# Ransom_Note_5.py

Given two stings ransomNote and magazine, return true if ransomNote can be constructed from magazine and false otherwise.
Each letter in magazine can only be used once in ransomNote.

Input Format
The input format is string The first line input is ransomeNote The second line input is magazine

Constraints
1 <= ransomNote.length, magazine.length <= 105 ransomNote and magazine consist of lowercase English letters.

Output Format
The output is boolean

# Count_Negative_Numbers_in_a_Sorted_Matrix.py

Given a string which is sorted in non-increasing order return the number of negative numbers.

Input Format
The input format is string separated with special character '#' and spaces

Constraints
none

Output Format
The output format is number

# Day 6
# Maximum_Answer.py

Our friend Monk has an exam that has quite weird rules. Each question has a difficulty level in the form of an Integer. Now, Monk can only solve the problems that have difficulty level less than X . Now the rules are-
Score of the student is equal to the maximum number of answers he/she has attempted without skipping a question. Student is allowed to skip just "one" question that will not be counted in the continuity of the questions. Note- Assume the student knows the solution to the problem he/she attempts and always starts the paper from first question.
Given the number of Questions, N ,the maximum difficulty level of the problem Monk can solve , X ,and the difficulty level of each question , A[i] can you help him determine his maximum score?

Input Format
First Line contains Integer N , the number of questions and the maximum difficulty X Monk can solve. Next line contains N integers, A[i]denoting the difficulty level of each question.

Constraints
None

Output Format
Maximum score Monk can achieve in the exam.

# Day 7
# Find_and_Count_Hashtags.py
Twitter shows trends in order to make its users aware of the trending news. These trends are nothing but trending hashtags that the users are tweeting about. For example: If thousands of users are talking about United States by adding a hashtag #US in their tweet, then US will be a trending hashtag. Couple of example tweets with hashtag #US could be:
Donald Trump becomes the 45th #US President Roger Federer wins #US Open for 5th time Given a list of N tweets, your task is to find top the five trending hashtags. Each tweet, let's call it S, will contain at least one one word with hashtag. There will be maximum of three hashtags in any tweet. All hashtags in a single tweet will be unique.
Note: 1. Any tweet is composed of lowercase and uppercase English letters, digits and spaces. 2. Any hashtag begins with # and the subsequent characters will only contain lowercase and uppercase English letters and digits.

Input Format
First line of the input will contain N denoting the number of tweets. Next N lines, each will contain a string S.

Constraints
where S denotes length of string S i.e. length of tweet. Any hashtag denoted by H, where H denotes length of any hashtag H.

Output Format
Print the top five trending hashtags. In case of tie between any two hashtags, print them in lexicographical order in a new line.

# Day 8
# Determining_Numbers.py

You are given an array of integers. The special property of the array is that exactly two different elements occur once while other elements occur twice.
You are required to determine those two elements.

Input Format
First line: Integer denoting the number of elements in the array Second line: space-separated integers denoting the values in the array

Constraints
None

Output Format
Print two space-separated integers that occur once in the array in ascending order.

# Day 9
# Maximum_Stamina.py

Humpy likes to jump from one building to another. But he only jumps to next higher building and stops when no higher building is available. Stamina required for a journey is xor of all the heights on which humpy jumps until he stops. If heights are [1 2 4], and he starts from 1, goes to 2 stamina required is 1⊕2=3, then from 2 to 3. Stamina for the entire journey is 1⊕2⊕4=7. Find the maximum stamina required if can start his journey from any building.

Input Format
First line: N, no of buildings. Second line: N integers, defining heights of buildings.

Constraints
None

Output Format
Single Integer that is the maximum stamina required for any journey.

# Day 10
# Mixing_Strings.py

Heisenberg is very fond of mixing various strings together. But he has storage problem. He wants that his strings use as less space as possible.
He has N strings right now. He wants to store them together. To reduce space he can use this property of mixing two strings:
Suppose he has string A="abcdef" and B="cdefghi". He can mix them to form "abcdefghi".
So, two strings can be mixed if some substring at the end of A is also at the starting of B which are mixed together.
Given the list of strings he has right now, print the minimum final characters he can get if he can mix any number of times, any of the given strings or the intermediate strings.

Input Format
First line contains N, the number of strings. Next N line contains, one string per line.

Constraints
None

Output Format
Print in one line the minimum final characters he can get if he can mix any number of times, any of the given strings or the intermediate strings.
