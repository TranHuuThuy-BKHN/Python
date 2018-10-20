# lớp cán bộ sẽ được kế thừa
class CanBo:

	def __init__(self, name = None, year = None, address = None):
		self.name = name
		self.year = year
		self.address = address

	#hiển thị các thông tin cơ bản của lớp cán bộ
	def intputIfo(self):
		print('name :', self.name)
		print('year :', self.year)
		print('address :', self.address)

	def getName(self):
		return self.name

	def setName(self, name):
		if name != None and len(name) > 0:
			self.name = name

	def getYear(self):
		return self.year

	def setYear(self, year):
		if year > 1970 : self.year = int(year)
	
	def getAddress(self):
		return self.address

	def setAddress(self, address):
		if address != None and len(address) > 0:
			self.address = address

#lớp kỹ sư kế thừa từ lớp cán bộ
class KySu(CanBo):

	numOfKS = 0

	def __init__(self, name = None, year = None, address = None, major = None):
		#gọi hàm tạo của lớp cha
		super().__init__(name, year, address)
		self.major = major		
		KySu.numOfKS += 1

	def getMajor(self):
		return self.major

	def setMajor(self, major):
		if major != None and len(major) > 0:
			self.major = major
			
	def intputIfo(self):
		print('Ky su so ', KySu.numOfKS)
		#gọi ham intputIfo của lớp cha
		super().intputIfo()
		print('major :', self.major)

#lớp công nhân kế thừa từ lớp cán bộ
class CongNhan(CanBo):
	
	numOfCN = 0

	def __init__(self, name = None, year = None, address = None, level = None):
		super().__init__(name, year, address)
		self.level = level
		CongNhan.numOfCN += 1

	def getLevel(self):
		return self.level
		
	def setLevel(self, level):
		if level != None and len(level) > 0:
			self.level = level

	def intputIfo(self):	
		print('Cong nhan so ', CongNhan.numOfCN)
		super().intputIfo()
		print('level : ', self.level)

#lớp nhân viên kế thừa từ lớp cán bộ
class NhanVien(CanBo):
	
	numOfNV	= 0	

	def __init__(self, name = None, year = None, address = None, typeWord = None):
		super().__init__(name, year, address)
		self.typeWord = typeWord
		NhanVien.numOfNV += 1

	def getTypeWord(self):
		return self.typeWord

	def setTypeWord(self, typeWord):
		if typeWord != None and len(typeWord) > 0:
			self.typeWord = typeWord

	def intputIfo(self):
		print('Nhan vien so ', NhanVien.numOfNV)
		super().intputIfo()
		print('typeWord : ', self.typeWord)
#=====================================================================================================================

'''
lớp QLCB cài đặt các phương thức thực hiện các chức sau:
- Nhập thông tin mới cho cán bộ (Hỏi người dùng muốn nhập cho: công nhân, kỹ sư hay nhân viên và
nhập đúng thông tin cho đối tượng đó).
- Tìm kiếm theo họ tên
- Hiển thị thông tin về danh sách các cán bộ
- Thoát khỏi chương trình.
'''
class QLCB:

	def __init__(self, listNV = [], listCN = [], listKS = [], select = -1):
		self.select = select
		self.listNV = listNV
		self.listKS = listKS
		self.listCN = listCN

		self.opcode = -1
		while True:
			print('1.Nhập thông tin')
			print('2.Tìm kiếm theo tên')
			print('3.Hiển thị thông tin')
			print('0.Thoát')
			self.opcode = int(input('Lựa chọn :'))

			if self.opcode == 1:
				print('Cán bộ muốn nhập thông tin')
				self.select = -1
				self.inPutCB()
			elif self.opcode == 2:
				name = input('Nhập tên tìm kiếm :')
				self.findCB(name)
			elif self.opcode == 3:
				self.outPut()
			else : break			

	#hàm thêm thông tin cán bộ
	def inPutCB(self):
		while self.select < 1 or self.select > 3:
			print('1.Nhan vien')
			print('2.Cong nhan')
			print('3.Ky su')
			self.select = int(input('Nhập lựa chọn :'))

		CB = CanBo()
		if 0 < self.select < 4:
			name = input('name : ')
			year = int(input('year : '))
			address = input('address : ')	 

		if self.select == 1:
			typeWord = input('typeWord : ')
			CB = NhanVien(name, year, address, typeWord)
			self.listNV.append(CB)

		elif self.select == 2:
			level = input('level : ')
			CB = CongNhan(name, year, address, level)
			self.listCN.append(CB)

		elif self.select == 3:
			major = input('major : ')
			CB = KySu(name, year, address, level)
			self.listKS.append(CB)				

	#hàm tìm cán bộ		
	def findCB(self, name = None):

		for nv in self.listNV:
			if name in nv.getName():
				print(nv.getName(), '(nv)')

		for ks in self.listKS:
			if name in ks.getName():
				print(ks.getName(), '(ks)')

		for cn in self.listCN:
			if name in cn.getName():
				print(cn.getName(), '(cn)')		

	#hàm hiển thị thông tin các cán bộ
	def outPut(self):
		print('===============Danh sách nhân viên===============')
		print('{:^20}{:^20}{:^20}{:^20}'.format('name', 'year', 'address', 'typeWord'))
		for nv in self.listNV:
			print('{:^20}{:^20}{:^20}{:^20}'.format(nv.getName(), str(nv.getYear()), nv.getAddress(), nv.getTypeWord()))

		print('===============Danh sách kỹ sư===============')
		print('{:^20}{:^20}{:^20}{:^20}'.format('name', 'year', 'address', 'major'))
		for ks in self.listKS:
			print('{:^20}{:^20}{:^20}{:^20}'.format(ks.getName(), str(ks.getYear()), ks.getAddress(), ks.major()))
		
		print('===============Danh sách công nhân===============')	
		print('{:^20}{:^20}{:^20}{:^20}'.format('name', 'year', 'address', 'level'))
		for cn in self.listCN:
			print('{:^20}{:^20}{:^20}{:^20}'.format(cn.getName(), str(cn.getYear()), cn.getAddress(), cn.level()))


	#hàm thoát khỏi chương trình
	def exit(self):
		pass		


qlcb = QLCB()