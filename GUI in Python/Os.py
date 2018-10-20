from os import *
from time import *
#hàm getcwd() trả về đường dẫn của thư mục chứa file hiện tại
# print(getcwd())#C:\Users\TranHuuThuy\Documents\Python\GUI in Python

# #hàm chdir(str) nhảy đến thư mục có tên str

# chdir('C:/Users/TranHuuThuy/Documents') 

# print(getcwd()) #C:\Users\TranHuuThuy\Documents

# #hàm listdir() trả về danh sách các thư mục con của thư mục hiện tại

# print(listdir())

# #hàm mkdir(str) tạo ra thư mục có tên str ở thư mục hiện tại, nếu mục hiện tại đã có file str thì lỗi
# mkdir('New')

# print(listdir())

# #hàm rename(str1, str2) thay tên thư mục str1 thành str2,nếu mục hiện tại chưa có file str thì lỗi

# rename('New', 'new2')
# print(getcwd())
# chdir('C:\\Users\\TranHuuThuy\\Documents')
# # sleep(10)
# # for i in range(10):
# # 	sleep(1)
# # 	#hàm makedirs(fd/cfd) dùng để tạo ra thư mục fd và thư mục con của fd là cfd, 
# # 	#nếu fd đã tồn tại rồi thì chỉ cần thêm thư mục con
# # 	makedirs('new/project' + str(i))
# # for i in range(10):
# # 	sleep(1)
# # 	rmdir('new/project'+str(9-i))	
# file_name = path.basename('/tmp/new/hello.txt')

file_path = getcwd()
print(file_path)
chdir('C:\\Users\\TranHuuThuy\\Documents\\Python\\')

mtime = path.getmtime(file_path)
print(ctime(mtime))