class getAllFunction():
    
    def Elegible():
        gender=str(input('Your Gender:'))
        age=int(input('Your Age:'))
        if gender.lower() == 'male':
            if age >= 21:
                return 'EILGIBLE'
            else:
                return 'NOT ELIGILBLE'
    
        elif gender.lower()=='girl':
            if age >=18:
                return 'EILGIBLE'
            else:
                return 'NOT ELIGILBLE'

    def percentage():
        sub1=int(input('Subject1='))
        sub2=int(input('Subject2='))
        sub3=int(input('Subject3='))
        sub4=int(input('Subject4='))
        sub5=int(input('Subject5='))
        total=sub1+sub2+sub3+sub4+sub5
        Percentage= float(total/5)
        print('Total :',int(total))
        print('Percentage :',f'{Percentage:.14f}')

    def OddEven():
        num=int(input('Enter a number:'))
        if (num%2)==1:
            # print('Odd Number')
            return f'{num} is Odd Number'
        else:
            # print('Even Number')
            return f'{num} is Even number '

    def subFields():
        print('Sub-fields in AI are:')
        print('Machine Learning')
        print('Neural Networks')
        print('Vision')
        print('Robotics')
        print('Speech Processing')
        print('Natural Language Processing')

    def triangle(Height,Breadth,Height1,Height2,Breadth1):
        print('Height:',Height)
        print('Breadth:',Breadth)
        area=float((Height*Breadth)/2)
        print('Area formula: (Height*Breadth)/2')
        print( f'Area of Triangle:  {area}')
        print('Height1:',Height1)
        print('Height2:',Height2)
        print('Breadth:',Breadth1)
        perimeter=Height1+Height2+Breadth1
        print('Perimeter formula: Height1+Height2+Breadth')
        print(f'Perimeter of Triangle:  {perimeter}')