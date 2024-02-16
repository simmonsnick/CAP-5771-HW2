
#Answer found in Q5 in Question Bank 1 (Tan et al, 2nd ed)
#import student_code_with_answers.utils as u
import utils as u

# Example of how to specify a binary with the structure:
# See the file INSTRUCTIONS.md
# ----------------------------------------------------------------------

def question1():
    """
    Note 1: Each attribute can appear as a node in the tree AT MOST once.
    Note 2: For level two, fill the keys for all cases left and right. If and attribute
    is not considered for level 2, set the values to -1. For example, if "flu" were the
    choice for level 1 (it is not), then set level2_left['flu'] = -1 level2_right['flu'] = -1.,
    and the same for keys 'flu_info_gain'.
    """
    answer = False
    answer = {}   
    level1 = {}
    level2_left = {}
    level2_right = {}
  
    level1["smoking"] = 1           #the average of yes and no entrophy
    level1["smoking_info_gain"] = 0.3

    level1["cough"] = -1            #the average of yes and no entrophy
    level1["cough_info_gain"] = 0.2

    level1["radon"] = -1            #the average of yes and no entrophy
    level1["radon_info_gain"] = 0.2

    level1["weight_loss"] = -1      #the average of yes and no entrophy
    level1["weight_loss_info_gain"] = 0.1

    level2_left["smoking"] = -1
    level2_left["smoking_info_gain"] = 0
    level2_right["smoking"] = -1
    level2_right["smoking_info_gain"] = 0

    level2_left["radon"] = 1
    level2_left["radon_info_gain"] = 0
    
    level2_left["cough"] = 1
    level2_left["cough_info_gain"] = 0.4
    
    level2_left["weight_loss"] = 1
    level2_left["weight_loss_info_gain"] = 0
    
    level2_right["radon"] = 0
    level2_right["radon_info_gain"] = 0.6

    level2_right["cough"] = 0
    level2_right["cough_info_gain"] = 0.1

    level2_right["weight_loss"] = 0
    level2_right["weight_loss_info_gain"] = 0

    
    answer["level1"] = level1
    answer["level2_left"] = level2_left
    answer["level2_right"] = level2_right

    # Fill up `construct_tree``  
    # tree, training_error = construct_tree()
    import utils as u
    tree = u.BinaryTree("smoking")  # MUST STILL CREATE THE TREE *****
    A = tree.insert_left("radon")
    B = tree.insert_right("cough")
    A.insert_left("y")
    A.insert_right("n")
    B.insert_left("y")
    B.insert_right("n")
    answer["tree"] = tree  # use the Tree structure
    # answer["training_error"] = training_error
    answer["training_error"] = 0  

    return answer

#Q1 Calculations 
#Entire Dataset
import math
entropy = -(5/10) * math.log2(5/10) - (5/10) * math.log2(5/10) 
#Smoking
split = -(4/5) * math.log2(4/5) - (1/5) * math.log2(1/5)
split = -(1/5) * math.log2(1/5) - (4/5) * math.log(4/5)
gain = entropy - split
print(gain)

#Chronic Cough
split = -(4/5) * math.log2(4/5) - (3/5) * math.log2(3/5)
split = -(1/5) * math.log2(1/5) - (2/5) * math.log2(2/5)
gain  = entropy - split
print(gain)
#Weight loss
split = -(3/5) * math.log2(3/5) - (2/5) * math.log2(2/5)
split = -(2/5) * math.log2(2/5) - (3/5) * math.log2(3/5)
gain = entropy - split
print(gain)

# ----------------------------------------------------------------------


def question2():
    answer = {}

    # Answers are floats
    answer["(a) entropy_entire_data"] = 1.425
    # Infogain
    answer["(b) x < 0.2"] = 0.177
    answer["(b) x < 0.7"] = 1.046
    answer["(b) y < 0.6"] = 1.783 

    # choose one of 'x=0.2', 'x=0.7', or 'x=0.6'
    answer["(c) attribute"] = "y = 0.6"  

    # Use the Binary Tree structure to construct the tree
    # Answer is an instance of BinaryTree
    import utils as u
    tree = u.BinaryTree("y < 0.6")
    answer["(d) full decision tree"] = tree
    tree = u.BinaryTree("y < 0.6")
    #L2 Left
    A = tree.insert_left("x < 0.7")
    #L2 Right
    B = tree.insert_right("x < 0.2")
    A.insert_left("y")
    A.insert_right("n")
    B.insert_left("y")
    B.insert_right("n")
    return answer

#Q2 Calculations 
#Entire Dataset
#Class A = 0.41, Class B = 0.46, Class C = 0.13
import math
entropy = -(0.41) * math.log2(0.41) - (0.46) * math.log2(0.46) - (0.13) * math.log2(0.13) 
print("total entropy")
print(entropy)
# x <= 0.2
entropy_r1 = -(0.16/0.2) * math.log2(0.16/0.2) - (0.04/0.2) * math.log2(0.04/0.2)
print(entropy_r1)
entropy_r2 =  -(0.09/0.8) * math.log2(0.09/0.8) - (0.3/0.8) * math.log2(0.3/0.8) - (0.41/0.8) * math.log2(0.41/0.8)
print(entropy_r2)
print('values for x<0.2')
print(entropy - 0.2*entropy_r1 - 0.8*entropy_r2)
# x <= 0.7
entropy_r3 = -(0.2/0.7) * math.log2(0.2/0.7) + (0.04/0.7) * math.log2(0.04/0.7) 
print(entropy_r3)
entropy_r4 = -(0.09/0.3) * math.log2(0.09/0.3) + (0.12/0.3) * math.log2(0.12/0.3) + (0.41/0.3) * math.log2(0.41/0.3)
print(entropy_r4)
print('values= for x<0.7')
print(entropy - 0.7*entropy_r3 - entropy_r4*0.3)
# y <= 0.6
entropy_r5 = -(0.32/0.4) * math.log2(0.32/0.4) + (0.04/0.4) * math.log2(0.04/0.4) + (0.04/0.4) * math.log2(0.04/0.4)
print(entropy_r1)
entropy_r6 = -(0.09/0.6) * math.log2(0.09/0.6) + (0.42/0.6) * math.log2(0.42/0.6) + (0.41/0.6) * math.log2(0.41/0.6)
print(entropy_r2)
print('values for y<0.6')
print(entropy - 0.4*entropy_r5 - entropy_r6*0.6)

# ----------------------------------------------------------------------

def question3():
    answer = {}

    # float
    answer["(a) Gini, overall"] = 0.5
    # float
    answer["(b) Gini, ID"] = 0.0
    answer["(c) Gini, Gender"] = 0.48
    answer["(d) Gini, Car type"] = 0.29
    answer["(e) Gini, Shirt type"] = 0.98

    answer["(f) attr for splitting"] = "Car Type"
    # Explanatory text string
    answer["(f) explain choice"] = "Car Type has a split at the root node which results in lowest impurity in Gini Index."

    return answer

#Calculations
#Entire Dataset
gini = 1 - (10/20)**2 - (10/20)**2 
#Part b
gini = 1 - (0/1)**2 - (1/1)**2
#Part c
gini_m = 1 - (6/10)**2 - (4/10)**2
gini_f = 1 - (4/10)**2 - (6/10)**2

#Part d
gini_f = 1 - (1/4)**2 - (3/4)**2
gini_s = 1 - (0/8)**2 - (8/8)**2
gini_l = 1 - (1/8)**2 - (7/8)**2

#Part e
gini_s = 1 - (3/5)**2 - (2/5)**2
gini_m = 1 - (3/7)**2 - (4/7)**2
gini_lg = 1 - (2/4)**2 - (2/4)**2
gini_xl = 1 - (2/4)**2 - (2/4)**2

# ----------------------------------------------------------------------
# Answers in th form [str1, str2, str3]
# If both 'binary' and 'discrete' apply, choose 'binary'.
# str1 in ['binary', 'discrete', 'continuous']
# str2 in ['qualitative', 'quantitative']
# str3 in ['interval', 'nominal', 'ratio', 'ordinal']


def question4():
    answer = {}
    # [string, string, string]
    # Each string is one of ['binary', 'discrete', 'continuous', 'qualitative', 'nominal', 'ordinal',
    #  'quantitative', 'interval', 'ratio'
    # If you have a choice between 'binary' and 'discrete', choose 'binary'

    answer["a"] = ['binary', 'qualitative', 'nominal']
    answer["a: explain"] = "Time is expressed in hours with two distinct categories."

    answer["b"] = ['continuous', 'quantitative', 'ratio']
    answer["b: explain"] = "Brightness is certain numerical measurement that takes on a range of values."

    answer["c"] = ['discrete', 'qualitative', 'ordinal']
    answer["c: explain"] = "The brightness measure is indicating an certain order of people judgments."

    answer["d"] = ['continous', 'quantitave', 'ratio']
    answer["d: explain"] = "The angle measures in degrees under any value within that range and takes on any real number."

    answer["e"] = ['discrete', 'qualitative', 'ordinal']
    answer["e: explain"] = "The medals has different levels of the achievement in a competition which are meaningful."

    answer["f"] = ['continous', 'quantitative', 'ratio']
    answer["f: explain"] = "The measure height above sea level has the values that are expressed in units which are numerical."

    answer["g"] = ['discrete', 'quantitative', 'ratio']
    answer["g: explain"] = "The number of patients has the certain amount of values that are countable and distinct."

    answer["h"] = ['discrete', 'qualitative', 'nominal']
    answer["h: explain"] = "ISBN is unique identifier that serves a book tracking and ordering."

    answer["i"] = ['discrete', 'qualitative', 'ordinal']
    answer["i: explain"] = "The pass light is consider a categorical into three level that indicate the visual properties."

    answer["j"] = ['discrete', 'qualitative', 'ordinal']
    answer["j: explain"] = "The miltary has different ranks which categorical and ordered classification of positions."

    answer["k"] = ['continous', 'quantitative', 'interval']
    answer["k: explain"] = "The distance from the center of campus can take on any real value within a given range."

    answer["l"] = ['discrete', 'quantitative', 'ratio']
    answer["l: explain"] = "The density of a substance measures the value which takes on any real number within a given range."

    answer["m"] = ['discrete', 'qualitative', 'norminal']
    answer["m: explain"] = "The coat check assigns a certain numeric label to the owner."

    return answer
# ----------------------------------------------------------------------

def question5():
    explain = {}

    # Read appropriate section of book chapter 3

    # string: one of 'Model 1' or 'Model 2'
    explain["a"] = "Model 2"
    explain["a explain"] = "In Model 2, has the better performance with the Dataset A has 0.98 accuracy."

    # string: one of 'Model 1' or 'Model 2'
    explain["b"] = "Model 2"
    explain["b explain"] = "Model 2 would have the high accuracy (A + B) = 0.85. So, I would choose the Model 1 for classification."

    explain["c similarity"] = "Model complexity estimate"
    explain["c similarity explain"] = " They both minimize more complexity models and makes a hyper parameter trade off models in complexity and accuracy."

    explain["c difference"] = "Model length estimate"
    explain["c difference explain"] = "MDL will minimize the total description length of the model, pessimitic estimates the generalization error rate in model."

    return explain


# ----------------------------------------------------------------------
def question6():
    answer = {}
    # x <= ? is the left branch
    # y <= ? is the left branch

    # value of the form "z <= float" where "z" is "x" or "y"
    #  and "float" is a floating point number (notice: <=)
    # The value could also be "A" or "B" if it is a leaf
    answer["a, level 1"] = "x <= 0.5"
    answer["a, level 2, right"] ="y < 0.4"
    answer["a, level 2, left"] = "x < A"
    answer["a, level 3, left"] = "y < B"
    answer["a, level 3, right"] = "x < 0.2"
    # run each datum through the tree. Count the number of errors and divide by number of samples. .
    # Since we have areas: calculate the area that is misclassified (total area is unity)
    # float between 0 and 1
    answer["b, expected error"] = 0.58
    # Use u.BinaryTree to define the tree. Create your tree.
    # Replace "root node" by the proper node of the form "z <= float"
    import utils as u
    tree = u.BinaryTree("x < 0.5")
    A = tree.insert_left("y < 0.4")
    B = tree.insert_right("x < A")
    answer["c, tree"] = tree
    return answer


# ----------------------------------------------------------------------
def question7():
    answer = {}

    # float
    answer["a, info gain, ID"] = 1.0
    answer["b, info gain, Handedness"] = 0.54

    # string: "ID" or "Handedness"
    answer["c, which attrib"] = "Handedness"

    # answer is a float
    answer["d, gain ratio, ID"] = 0.46
    answer["e, gain ratio, Handedness"] = 0.46

    # string: one of 'ID' or 'Handedness' based on gain ratio
    # choose the attribute with the largest gain ratio
    answer["f, which attrib"] = "neither"

    return answer

# ----------------------------------------------------------------------

if __name__ == "__main__":
    answers = {}
    answers["q1"] = question1()
    answers["q2"] = question2()
    answers["q3"] = question3()
    answers["q4"] = question4()
    answers["q5"] = question5()
    answers["q6"] = question6()
    answers["q7"] = question7()
    
    u.save_dict("answers.pkl", answers)
