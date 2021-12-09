import glob
import os
import json
import random
import string
from tqdm import tqdm
import xml.etree.ElementTree as ET






# dir='C:/Users/STAFF/Desktop/NishaPatel/NIsha/output_img_folder/'
# mylist=glob.glob(os.path.join(dir,'*.xml'))

# os.chdir("C:/Users/STAFF/Desktop/NishaPatel/NIsha/output_img_folder")
# image_file=glob.glob("*.jpg")




# full_dic={}    
# id=0
# maindic={}

# seperator=","
# tag_list=[]

# for mytree in mylist:
    
#     objectlist=[]
#     i=1
#     with open(mytree) as f:
#         myroot=ET.parse(f)
#         ot=myroot.findall("object")
#         width1=int(myroot.find("size/width").text)
#         height1=int(myroot.find("size/height").text)
#         image=myroot.find("filename").text
        
        
#         for objects in ot:

            
#             name=objects.find("name").text


#             Xminval=float(objects.find("bndbox/xmin").text)

#             Yminval=float(objects.find("bndbox/ymin").text)

#             Xmaxval=float(objects.find("bndbox/xmax").text)

#             Ymaxval=float(objects.find("bndbox/ymax").text)

#             lists1={"x1":Xminval,"y1":Yminval,"x2":Xmaxval,"y2":Ymaxval,"width":width1,"height":height1,
#             "box":{"x1":Xminval,"y1":Yminval,"x2":Xmaxval,"y2":Ymaxval},
#             "points":[{"x":Xminval,"y":Yminval},{"x":Xmaxval,"y":Yminval},{"x":Xmaxval,"y":Ymaxval},{"x":Xminval,"y":Ymaxval}],"UID":''.join(random.choices(string.digits, k=8)),"id":id,"type":"rect","tags":[name],"name":i}
            
#             i=i+1
#             id=id+1
    
#             objectlist.append(lists1)
            # tag_list.append(name)
#         masterdic={image:objectlist}
        
#     maindic.update(masterdic)
    

# new_set=set(tag_list)

# new_set=list(new_set)

# new_set=seperator.join(new_set)

# temp_dic={"frames":maindic,"framerate":"1","inputTags":new_set,"suggestiontype":"track","scd":False,"visitedFrames":image_file,"tag_colors":["#0ed78c","#a2099a"]}
# full_dic.update(temp_dic)
# #print(full_dic)

# with open('C:/Users/STAFF/Desktop/NishaPatel/NIsha/json1.json','w') as outfile:
#     json.dump(full_dic,outfile)

def fun():
    with open("C:/Users/STAFF/Desktop/NishaPatel/original_jsonfile/output_img_folder.json", "r") as read_file:

        dic_file= json.load(read_file)
        # string_file=json.dumps(dic_file)

        key=dic_file["frames"]
        for image_name in tqdm(key,"Making text"):
            
            value=key[image_name]
            
            x1=0
            x2=0
            y1=0
            y2=0
            new_object_list=[]
            for dictionary_item in value:

                x1=dictionary_item["x1"]
                x2=dictionary_item["x2"]
                y1=dictionary_item["y1"]
                y2=dictionary_item["y2"]
                tag=dictionary_item["tags"]
                new_tag=str(tag)[2:-2]
                
                object_list=[x1,y1,x2,y2,new_tag]
                
                
                
                image_list=[image_name,x1,y1,x2,y2,new_tag]
        
                new_object_list.append(object_list)
            result=[image_name,new_object_list]
            
            string_list=" ".join(str(new_list1) for new_list1 in result)
            
            # print(string_list)



            with open("C:/Users/STAFF/Desktop/NishaPatel/NIsha/image_file.txt", "a") as textfile:

                textfile.writelines(string_list)
                textfile.write('\n')


            with open("C:/Users/STAFF/Desktop/NishaPatel/NIsha/image_file.txt","r") as text_file_read:
                lines=text_file_read.read()
                lines=lines.replace(", ",",")
                # lines=lines.replace("[["," ")
                lines=lines.replace("]","")
                lines=lines.replace("[","")
                lines=lines.replace(" ",",")
            with open("C:/Users/STAFF/Desktop/NishaPatel/NIsha/image.txt", "w") as textfile:
                textfile.writelines(lines)
                textfile.write('\n')





    # trash_list=[]
def trail():
    file_read=open("C:/Users/STAFF/Desktop/NishaPatel/NIsha/image.txt","r") 
    first_line=file_read.read()
    # first_list=[x for x in map(str.strip, first_line.split('\n')) if x]
    first_list=[x for x in first_line.split('\n')]
    # print(first_list)
    master={}
    # imglist=[]
    taglist=set()
    imagelist=[]
    id_1=0
    main_dic_list={}
    for n in range(len(first_list)):
        # new_name=0
        file_name=first_list[n].split(",")
        print(file_name)
        image_file_name=file_name[:1]
        image_file_name=",".join(image_file_name)
        print(image_file_name)    
        imagelist.append(image_file_name)
    # print(imagelist)
        l=len(file_name)
        print(l)
        l=l-1
        l=int(l/5)
        master_object_list=[]
        if len(file_name)<5:
            id_1+=1
            object_dic=[]
            master_object_list.append(object_dic)
            temp={file_name[0]:master_object_list}
            main_dic_list.update(temp)
        else:
            j=1 
            tag_index=5
            # master_object_list=[]
            for i in range(l):
                new_name=i+1
                Xmax=file_name[j]
                # print(Xmax)
                Ymax=file_name[j+1]
                # print(Ymax)
                Xmin=file_name[j+2]
                # print(Xmin)
                Ymin=file_name[j+3]
                # print(Ymin)
                tag=file_name[tag_index]
                j=j+5
                tag_index=tag_index+5
                newtag=tag.replace("'","").strip()
                taglist.add(newtag)  
                tag_set=list(taglist)
                tag_set=",".join(tag_set)
                object_dic={"x1":float(Xmax),"y1":float(Ymax),"x2":float(Xmin),"y2":float(Ymin),"width":1280,"height":720,"box":{"x1":float(Xmin),"y1":float(Ymin),"x2":float(Xmax),"y2":float(Ymax)},
                "points":[{"x":float(Xmin),"y":float(Ymin)},{"x":float(Xmax),"y":float(Ymin)},{"x":float(Xmax),"y":float(Ymax)},{"x":float(Xmin),"y":float(Ymax)}],
                "UID":''.join(random.choices(string.digits, k=8)),"id":id_1,"type":"rect","tags":[newtag],"name":new_name}
                id_1+=1
                master_object_list.append(object_dic) 
            temp={image_file_name:master_object_list}
            # main_dic_list.update(temp)       
        master.update(temp)
    fulldic={"frames":master,"framerate":"1","inputTags":tag_set,"suggestiontype":"track","scd":False,"visitedFrames":imagelist,"tag_colors":["#0ed78c","#a2099a"]}
    # print(fulldic)
    # print(imagelist)
    # print(imagelist)
    outputfile=open('C:/Users/STAFF/Desktop/NishaPatel/NIsha/newjson/json_file.json','w') 
    json.dump(fulldic,outputfile)

if __name__ == "__main__":
    fun()
    trail()











































