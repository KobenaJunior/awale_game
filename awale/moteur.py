class MoteurAwale():
	# MOTEUR DE JEU Version 2
	
	def jeu(self,plateau,tour,pointA,pointB,idx):
		# global tour
		self.plateau=plateau
		self.tour=tour
		self.pointA=pointA
		self.pointB=pointB
		self.last_index=[]

		is_joueur_A=(self.tour%2==0)
		camp=range(0,6) if is_joueur_A else range(6,12)

		if(idx not in camp or self.plateau[idx]==0):
			return None,None,None,None
		lst_indx,point_gagne=self.distribution(idx,camp)

		if(is_joueur_A):
			self.pointA+=point_gagne
			print(f"reflexion: pour le coup:{idx} on obtiens {self.pointA}, ")
			print(f"plateau:{self.plateau}\n")
		else:
			self.pointB+=point_gagne
		return self.plateau,self.pointA,self.pointB,lst_indx


	def capture(self,index):
		point=0
		if(index in range(0,6)):
			table=range(0,index+1)
		elif(index in range(6,12)):
			table=range(6,index+1)
		for i in table[::-1]:
			if(self.plateau[i] in range(2,4)):
				# print(f"capture de {self.plateau[i]} pions pour{self.tour}\n")
				point+=self.plateau[i]
				self.plateau[i]=0
			else:
				break
		return point
		# print("capture")

	def distribution(self,index,intervalle):
		# global tour,pointA,pointB
		n=1
		index_initial=index
		
		for i in range(self.plateau[index]):
			if(len(self.plateau[index+n:])==0):
				n=0
				index=0
			self.plateau[index+n]+=1
			n+=1
		self.plateau[index_initial]=0
		last_index=index+n-1
		# print(f"last_index: {last_index}, {self.plateau[last_index]} pions\n")
		
		p=0
		if(last_index not in intervalle and self.plateau[last_index]>1):
			# if(self.plateau[last_index]==1):
			# 	pass
			if(self.plateau[last_index] in range(2,4)):
				p=self.capture(last_index)
			else:
				self.distribution(last_index,intervalle)
		# print(f"plateau: {self.plateau}, pions restant {sum(self.plateau)},point A: {self.pointA} point B {self.pointB}\n")
		# print(f"plateau: {self.plateau}")
		l=last_index
		self.last_index.append(l)
		# print(f'the lasttttttt is:{l} and table last_ id: {self.last_index}')
		return self.last_index[0],p
