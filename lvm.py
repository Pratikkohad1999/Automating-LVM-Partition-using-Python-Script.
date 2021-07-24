import os
os.system("tput setaf 3")
os.system("tput setab 8")

print("		 ---------------------------		")
print("		|     Welcome To LVM Menu   |		")
print("		 ---------------------------		")
print("*"*50)
ch="y"

print( """ 
ENTER 1: To See all the available disks
ENTER 2: To Create Physical Volume
ENTER 3: To See Physical Volume
ENTER 4: To Launch Volume Group
ENTER 5: To See Volume Group
ENTER 6: To Launch Logical Volume
ENTER 7: To See Logical Volume
ENTER 8: To mount the disk
ENTER 9: To format the partition
ENTER 10: To extend the size of Logical Volume
""")

while ch=='y':
	
	choice=int(input("Enter your choice:"))
	if choice==1:
		os.system("lsblk")
	elif choice==2:
		try:
			pvname=input("Enter Physical Volume name:")
		except:
			print("Enter name properly!!")
		else:
			os.system(f"pvcreate /dev/{pvname}")
	
	elif choice==3:
		try:
			pvname=input("Enter Physical Volume name:")
		except:
			print("Enter name properly!!")
		else:
			os.system(f"pvdisplay /dev/{pvname}")
		
	elif choice==4:
		try:
			vgname=input("Enter volume group name:")
			pvname=input("Enter Physical Volume name:")
		except:
			print("Enter info properly!!")
		else:
			os.system(f"vgcreate {vgname} /dev/{pvname}")

	elif choice==5:
		try:
			vgname=input("Enter volume group name:")
		except:
			print("Enter info properly!!")
		else:
			os.system(f"vgdisplay {vgname}")
	elif choice==6:
		try:
			lvname=input("Enter lv name:")
			vgname=input("Enter volume group name:")
			size=int(input("Enter size of the volume:"))
		except:
			print("Enter info properly!!")
		else:
			os.system(f"lvcreate --size {size}G --name {lvname} {vgname}")
		
	elif choice==7:
		try:
			lvname=input("Enter lv name:")
			vgname=input("Enter volume group name:")
		except:
			print("Enter info properly!!")
		else:
			os.system(f"lvdisplay {vgname}/{lvname}")

	elif choice==8:
		try:
			lvname=input("Enter lv name:")
			vgname=input("Enter volume group name:")
			folder=input("Enter directory name to which u want to mount")
		except:
			print("Enter info properly!!")
		else:
			os.system(f"mount /dev/{vgname}/{lvname} /{folder}")

	elif choice==9:
		try:
			frmt=input("What do u want to format(enter full path):")
		except:
			print("enter proper name!!")
		else:
			os.system(f"mkfs.ext4 {frmt}")
	elif choice==10:
		try:
			lvname=input("Enter lv name:")
			vgname=input("Enter volume group name:")
			size=int(input("Enter size of the volume:"))
		except:
			print("Enter details properly!!")
		else:
			os.system(f"lvextend --size +{size}G /dev/{vgname}/{lvname}")
			os.system("resize2fs /{vgname}/{lvname}")
		
	else:
		print("CHOICE INVALID !!!")
	ch=input("do you want to continue:(y/n)")
