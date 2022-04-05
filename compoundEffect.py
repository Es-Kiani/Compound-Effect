import datetime
import os

def writeToFile(data:str, path=os.getcwd(), fName="Result.txt", fOType="a+"):
    with open(f"{path}/{fName}", fOType) as file:
        file.write(str(data))
    return
    


def CompoundEffect(got_Asset, got_Percent, got_Step) -> float:
    now_Time = datetime.datetime.now()
    asset, percent, step = abs(got_Asset), abs(got_Percent), abs(got_Step)
    
    writeToFile(f"{now_Time}: \n")
    writeToFile(f"asset:{got_Asset} percent:{got_Percent} step:{got_Step}  \n")
    
    for i in range(1, step + 1):
        pAsset = asset
        p = percent * (asset / 100)
        asset += p
        writeToFile(f"Step{i}: {round(pAsset, 1)}\t+\t{got_Percent}%({round(p, 1)})\t=\t{round(asset, 1)}  \n")

    writeToFile(f"\n\n")
    
    return round(asset, 1)
    
    
if __name__ == "__main__":
    print(CompoundEffect(-50000, -1, -30))
