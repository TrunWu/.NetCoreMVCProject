from os import listdir
from os.path import isfile,join

def funPrint(path,folder):
	for f in listdir(path):
		fname = f.strip(".cs")
		print("public DbSet<coderush.Models.%s.%s> %s{ get; set; }"%(folder,fname,fname))

accountPath = "./coderush/Models/AccountViewModels"
ManagePath = "./coderush/Models/ManageViewModels"
SyncfusionPath = "./coderush/Models/SyncfusionViewModels"

funPrint(accountPath,"AccountViewModels")
funPrint(ManagePath,"ManageViewModels")
funPrint(SyncfusionPath,"SyncfusionViewModels")
