def apply(x):     
        while True:
            y=int(input('请输入第一个数字'))
            z=int(input('请输入第二个数字'))   
          
            if x==1:
                print('{}+{}={}'.format(y,z,y+z))
            
            elif x==2:
                print('{}-{}={}'.format(y,z,y-z))
    
            elif x==3:
                print('{}*{}={}'.format(y,z,y*z))
        
            elif x==4:
                print('{}/{}={}'.format(y,z,y/z))
                
            else:
                print('请再输入一遍')
            break

x=int(input('请输入选项'))       

apply(x)
        
        