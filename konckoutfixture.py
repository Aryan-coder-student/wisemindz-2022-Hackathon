# Programme of knockout tournament fixture of odd teams
import random # this module would be used to decide winner in every match
import math # this will convert float to int 
import time
from more_itertools import grouper # this module would be used create the pair 
N = int(input("No. of team in the tournament :")) # --> No. of team playing
while(N%2==0):
    print("Enter odd no. of teams ")
    N = int(input("No. of team in the :"))
team_list =[] #--> Store the name of teams
byesupper=[] #---> Store no. of Bye and then remove.
byesupper_l=[] #---> Store no. of Bye and then remove.
for i in range(0,N):
    team = input("Enter the name of the team : ")
    if len(team)==0:
        print("Please enter the team's name")
        team = input("Enter the name of the team : ")
        team_list.append(team)
    else:
        team_list.append(team)
#=====================================================================================Search whether same team is entered more than once 

#======================================================================================= 
team_list_sort = team_list.sort()
upper_half = math.ceil((N+1)/2) # NO. of teams in upper half 
lower_half = math.ceil((N-1)/2) # NO. of teams in lower half
list_upper_half = [] # Store upper half teams.
list_lower_half = [] # Store lower half teams
list_bye_teamup=[] # Store the team that got bye in upper half
list_bye_teamlower=[] # Store the team that got bye in lower half

#=========================================================================================================================
for j in range(0,N): # Calculate the power of 2
    if (math.pow(2,j)>=N):
        n = math.pow(2,j) 
        break
bye_in_tournament=n-N # --> Calculate no. of byes. Formula to calculate byes is 2^n-teams
print("No. of byes in the tornament is : ",bye_in_tournament)
time.sleep(1.7)
print("No. of rounds would be : ",j) # According to defination power of two will be the no. of round
time.sleep(1.7)
print("No. of matches would be : ",N-1) # total no. of matches-> total no. of team - 1
time.sleep(1.7)
#===========================================================================================================================Splitting teams in upper half and lower half
for x in range(0,math.ceil(upper_half)):
    list_upper_half.append(team_list[x]) # -->Upper half team 
for y in range (math.ceil(lower_half) + 1,N):
    list_lower_half.append(team_list[y]) # -->lower half team
#-=============================================================================================================================Byes
b_u = math.ceil((bye_in_tournament-1)/2) #----------------- No. of Byes in upperhalf

b_l = math.ceil((bye_in_tournament+1)/2) #----------------- No. of Byes in lower half
time.sleep(1.7)
print((bye_in_tournament-1)/2,"Byes in upper half")
for i in range(0,b_u): 
    b = "Bye"
    byesupper.append(b)
time.sleep(1.7)
print(list_upper_half,"-->UPPER HALF")    
time.sleep(1.7)
print((bye_in_tournament+1)/2,"Byes in lower half") #-------------------- No. of Byes in lower half 
for i2 in range(0,math.ceil((bye_in_tournament+1)/2)):
    b = "Bye"
    byesupper_l.append(b)
time.sleep(1.7)
print(list_lower_half,"-->LOWER HALF")
#================================================================================================================================Giving byes to the upper teams
b = b_u - 1
b_1 = b_l - 1
if b==0:
    b = b_u
elif b_1==0:
    b_1 =b_l
for disbye in range(0,b): #-->this will distribute the byes in upper half according to rule.
#First bye will be give to first,then next to the last element of the list,then again to second elment and then to second last element this will go on untill byesupper get empty
    if len(byesupper)==0:
        break
    else:
        low_bye = list_upper_half[disbye],byesupper[0]
        list_bye_teamup.append(low_bye)
        byesupper.remove(byesupper[-1]) #--->As 1 team got bye, one bye would be removed from bysupper list 
        list_upper_half[disbye] = low_bye # -->this would remove the element from index and replace it with ("removed element" , "Bye")
        if len(byesupper)==0: # the loop will break when byesupper get empty (i.e When all byes is ditributed)
            break
        high_bye = list_upper_half[upper_half-1],byesupper[-1]
        list_upper_half[upper_half-1] = high_bye
        byesupper.remove(byesupper[-1])
        list_bye_teamup.append(high_bye)
        upper_half = upper_half -1
time.sleep(1.7)
print(list_upper_half,"---Teams byes distribution")
time.sleep(1.7)
#-================================================================================================================Giving byes to lower half team
for disbye_l in range(0,b_1):#-->thos will distribute the byes in lower half according to rule.
#First bye will be give to first,then next to the last element of the list,then again to second elment and then to second last element this will go on untill byesupper get empty
    if len(byesupper_l)==0:
        break
    else:
        low_bye_lower = list_lower_half[disbye_l],byesupper_l[0] #--->this will distribute bye from index 0
        list_bye_teamlower.append(low_bye_lower)
        byesupper_l.remove(byesupper_l[-1])#--->As 1 team got bye, one bye would be removed from bysupper list 
        list_lower_half[disbye_l] = low_bye_lower # -->this would remove the element from index and replace it with ("removed element" , "Bye")
        if len(byesupper_l)==0:
            break
        high_bye_lower = list_lower_half[lower_half-1],byesupper_l[-1]#--->this will distribute bye from last index
        list_lower_half[lower_half-1] = high_bye_lower #-->this would remove the element from index and replace it with ("removed element" , "Bye")
        byesupper_l.remove(byesupper_l[-1])#--->As 1 team got bye, one bye would be removed from bysupper list 
        list_bye_teamlower.append(high_bye_lower)
        lower_half = lower_half -1 # iterate backward to replcae element
print(list_lower_half,"---Teams byes distribution")
time.sleep(1.7)
#======================================================================================================================Code for matches between none bye teams        
print("First match will be between these Teams (None from byes) : ")
time.sleep(1.7)
match_1=[] #list of teams who don't have bye
#Since first round will be between those team who don't get bye so we have to choose those team who don't get byes
for pair in list_upper_half:
    if "Bye" not in pair: #----This would find thise teame who don't have byes  in upper half and then put the team in match_1 list
        match_1.append(pair)
for pair_1 in list_lower_half:
    if "Bye" not in pair_1: #----This would find thise teame who don't have byes  in lower half and then put the team in match_1 list
        match_1.append(pair_1)
print(list(grouper(match_1,2)))
time.sleep(1.7)
#====================================================================================================================Rounds that include byes
match_1_result = [m[random.randint(0,1)] for m in grouper(match_1,2)] # this would randomly select teams from match_1 
for pair_2 in list_bye_teamup: # Now in second round team who got Byes will play so we have to include them  
     if "Bye"in pair_2: # this woul found the team who have bye in list_bye_teamup and then include it in match_1_result
            match_1_result.append(pair_2)
for pair_3 in list_bye_teamlower:# Now in second round team who got Byes will play so we have to include them 
     if "Bye"in pair_3:# this woul found the team who have bye in list_bye_teamlower and then include it in match_1_result
            match_1_result.append(pair_3)
match_1_result.sort(key=lambda x: x[0] if isinstance(x, tuple) else x) # ---> this will sort the list so that sequence not get diturbed 
s_r = list(grouper(match_1_result,2)) # ---this will make pairs of teams that would play with each other
time.sleep(1.7)
print(s_r, "-----> Result after previous round 1")
time.sleep(1.7)
match_2_result = [mn[random.randint(0,1)] for mn in grouper(match_1_result,2)]# -->this will randomly choose the team from each sublist.
match_4_result =list(grouper(match_2_result,2))# ---.now the teams in list match_2_result will have match ,so again we have to make pair 
match_2_result.clear() #---> clear the list
match_2_result.append(match_4_result) #---> replace match_2_result list with match_4_result list
print(match_2_result) 
time.sleep(1.7)
while len(match_4_result)>1: #--> This loop statment run till actual rounds-2 and replace the list again and till we get winner 
    new_matches=[]
    for ij in range(math.ceil(len(match_4_result)/2)):
        new_matches.append((random.choice(match_4_result[2*ij]),random.choice(match_4_result[2*ij+1])))
    match_4_result=new_matches
    time.sleep(1.7)
    print(match_4_result)
match_4_result=[random.choice(match_4_result[0])]
time.sleep(1.7)
print(match_4_result,"---> Winner") # --->Our final winner

            
                            


        
        

        
    
    
