from os import system
class Tic_Tac_Toe:
	def board(self,l):
		print('Tic Tac Toe'.center(65))
		print("\n")
		print('_'*14)
		print('|',end='')
		for i in range (1,len(l)+1):
			if(i==3 or i==6 ):
				print(i,' | ')
				print('_'*14)
				print('|',end='')
			else:print(i,' | ',end='')
		print('\n','_'*14)
	def game(self,l,name1,name2):
		c,pos=0,0
		valid_pos=[1,2,3,4,5,6,7,8,9]
		x=['X','X','X']
		o=['O','O','O']
		while c<9:
			pos=int(input('Enter Position :-	'))
			if pos not in valid_pos:
				print('Enter Valid Position')
				c-=1
				continue
			else:
				if c<0:
					l[pos-1]='X'
					valid_pos.remove(pos)
					c=0
				elif c%2==0:
					l[pos-1]='X'
					valid_pos.remove(pos)
				else :
					l[pos-1]='O'
					valid_pos.remove(pos)
			win_pos=[[l[0],l[1],l[2]],[l[3],l[4],l[5]],[l[6],l[7],l[8]],
					[l[0],l[3],l[6]],[l[1],l[4],l[7]],[l[2],l[5],l[8]],
					[l[0],l[4],l[8]],[l[2],l[4],l[6]]]
			system('cls')
			print('_'*14)
			print('|',end='')
			for i in range (len(l)):
				if(i==2 or i==5 ):
					print(l[i],' | ')
					print('_'*14)
					print('|',end='')
				else:print(l[i] ,' | ',end='')
			print('\n','_'*14)
			if(x in win_pos):
				print(f'{name1}  won')
				return 1
			elif(o in win_pos):
				print(f'{name2}  won')
				return 0
			c+=1
		else:
			print("Draw")
			return -1
if __name__=="__main__":
	g=Tic_Tac_Toe()
	l=[' ',' ',' ',' ',' ',' ',' ',' ',' ']
	name1=input('Enter Player1 name :-	')#'x'
	name2=input('Enter Player2 name :-	')#'o'
	system('cls')
	cont='yes'
	x1,o1,d1=0,0,0
	while(cont.lower().strip() !='no'):
		l=[' ',' ',' ',' ',' ',' ',' ',' ',' ']
		g.board(l)
		m=g.game(l,name1,name2)
		if(m==1):
			x1+=1
		elif(m==0):
			o1+=1
		else:
			d1+=1
		cont=input('Did you want to Continue playing.Enter yes or no\n')
	print('GAME OVER')
	print(f"{name1} score :- ",x1)
	print(f"{name2} score :- ",o1)
	print("Draws :- ",d1)
	if(x1>o1):
		print(f"{name1} Won")
	elif(o1>x1):
		print(f"{name2} Won")
	else:
		print('Draw!!')
