class FindPercent():
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