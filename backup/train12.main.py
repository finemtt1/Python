#主程式
#封包:包含模組的資料夾，在資料夾產生 ini.py 形成封包
import geometry.point
result=geometry.point.distance(3,4)
print("distance:",result)
import geometry.line as line #as 別名
result=line.slope(1,1,3,3)
print("slope:",result)