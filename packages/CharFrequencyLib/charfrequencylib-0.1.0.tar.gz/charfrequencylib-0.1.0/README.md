# CharFrequencyLib
مكتبة لحساب تكرار كل حرف في نص. 

## التثبيت
pip install CharFrequencyLib 

## CMD
charfrequencylib "hello"
# 'h':1
# 'e':1
# 'l':2
# 'o':1 

## Python
from char_frequency_lib import char_frequency
text = "hello"
print(char_frequency(text))  
# {'h':1, 'e':1, 'l':2, 'o':1} 
