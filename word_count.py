count_dict={}
count_dict_person1={}
count_dict_person2={}

mssgs=open("WhatsApp Chat with Person.txt","r",encoding="utf-8")
person1="person1:" #change to names in text file
person2="person2:"


for line in mssgs:

    #combined word count for both people
    for word in line.split(":")[-1].strip().split():
        if word not in count_dict:
            count_dict[word]=1
        else:
           count_dict[word]=count_dict[word]+1

    if len(line.split(person1))==2: # won't work where there are new lines within a message
        
        for word in line.split(person1)[1].strip().split():
            if word not in count_dict_person1:
                count_dict_person1[word]=1
            else:
               count_dict_person1[word]=count_dict_person1[word]+1

    elif len(line.split(person2))==2:
        
        for word in line.split(person2)[1].strip().split():
            if word not in count_dict_person2:
                count_dict_person2[word]=1
            else:
               count_dict_person2[word]=count_dict_person2[word]+1

print("done, now saving")
results_combined=open("results_combined.txt","w",encoding='utf-8')
results_person1=open("results_person1.txt","w",encoding='utf-8')
results_person2=open("results_person2.txt","w",encoding='utf-8')


for i in sorted(count_dict.items(), key=lambda x: x[1], reverse=True): #most commonly used words at top of file
    results_combined.write(str(i)+"\n")
    
for i in sorted(count_dict_person1.items(), key=lambda x: x[1], reverse=True):
    results_person1.write(str(i)+"\n")

for i in sorted(count_dict_person2.items(), key=lambda x: x[1], reverse=True):
    results_person2.write(str(i)+"\n")

results_combined.close()
results_person1.close()
results_person2.close()
print("saved")
