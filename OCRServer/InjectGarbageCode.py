#!/usr/bin/env python
# _*_ coding:utf-8 _*_

import random
import os
import string
import sys
import socket
import time

array = []
projectPath = '/Users/apple/Desktop/test/'
classArray = ['NSString','UILabel','NSDictionary','NSData','UIScrollView','UIView']
defaultNewClassCount = 50;
defautlPropertNum = 10;
defaultMethodNum = 50;
defaultProjectName = "projecttest001";



# print sys.argv
#
# for i in sys.argv:


def createNameArr():
    first = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    second = "abcdefghijklmnopqrstuvwxyz"
    number = "345"
    index = 0
    for i in range(500):
        final = (random.choice(first))
        index = random.randint(3, 5)
        for i in range(index):
            final += (random.choice(second))
        final += (random.choice(first))
        for i in range(index):
            final += (random.choice(second))
        array.append(final)

    print (array)

def createPropertArr():
    propryNameArray = []
    for index in range(0, defautlPropertNum):
        propryNameArray.append(random.choice(array))
        propryNameArray = list(set(propryNameArray))
    return propryNameArray


def createMethodArr():
    methodNameArray = []
    for index in range(0, defaultMethodNum):
        methodNameArray.append(random.choice(array))
        methodNameArray = list(set(methodNameArray))
    return  methodNameArray

def createFileH(profectPath,projectName,className,nextClass,propryArr,methodArr,isFirstClass):
    full_path = profectPath + className + '.h'
    print (full_path)
    file = open(full_path, 'w')
    # pcname = socket.getfqdn(socket.gethostname())
    hostname = socket.gethostname()
    thisTime = time.strftime('%Y/%m/%d', time.localtime(time.time()))

    #写注释
    if isFirstClass == 1:
        file.write('//firstClass %s' % className)

    file.write(
        '//\n//  ' + className + '.h\n// '+ projectName +'\n\n//  Created by ' + hostname +' on '+ thisTime +'.\n//  Copyright ©  dr. All rights reserved.\n//\n\n')
    file.write("#import <Foundation/Foundation.h>\n")
    file.write("#import <UIKit/UIKit.h>\n")

    if nextClass != "":
        file.write('#import "%s.h"\n' % nextClass)

    # file.write("#import <UIKit/UIKit.h>\n")
    file.write("@interface ")
    file.write("%s : NSObject\n" % className)
    for propertyName in propryArr:
        file.write('@property(nonatomic,strong)' + random.choice(classArray) + ' * ' + propertyName + ';\n')
    file.write('\n\n')

    n = len(methodArr)

    for i in range(0, n):
        methodName = methodArr[i]
        if i == 0:
            file.write('-(double)' + methodName + '_first:(double)vaule;\n')
        else:
            file.write('-(double)' + methodName + ':(double)vaule;\n')

    # for methodName in methodArr:
    #     # file.write('- (void)pushTo' + methodName + 'VC:(NSDictionary *)info;\n')
    #     file.write('-(double)' + methodName +':(double)vaule;\n' )
    file.write("@end")
    file.close()
    print('Done')


#创建.m文件
def createFileM(profectPath,projectName,className,nextClass,propryArr,methodArr,nextMethod):
    full_path = profectPath + className + '.m'
    file = open(full_path, 'w')
    hostname = socket.gethostname()
    thisTime = time.strftime('%Y/%m/%d', time.localtime(time.time()))
    file.write(
        '//\n//  ' + className + '.h\n// ' + projectName + '\n\n//  Created by ' + hostname + ' on ' + thisTime + '.\n//  Copyright ©  dr. All rights reserved.\n//\n\n')
    file.write('#import "%s.h"' % className)

    # file.write("%s : NSObject\n" % className)


    file.write("\n@implementation ")
    file.write("%s : NSObject\n" % className)

    n = len(methodArr)

    for i in range(0,n):
        methodName = methodArr[i]
        number = random.randint(1, 4)

        operatorArr = ['+', '*', '/']

        operator = random.choice(operatorArr)

        if i == 0:
            file.write('-(double)' + methodName + '_first:(double)vaule\n{\n\n')
        else:
            file.write('-(double)' + methodName + ':(double)vaule\n{\n\n')


        if i + 1 < n:
            file.write('double result = vaule %s %s;\n' % (operator, number))
            otherMethod = methodArr[i + 1];
            file.write('\nresult = [self '+ otherMethod + ':result];\n')

        else:
            if nextClass != "":
                file.write('double result = vaule %s %s;\n' % (operator, number))
                file.write('%s *obj = [[%s alloc]init];\n' %(nextClass,nextClass))
                file.write('result = [obj %s_first : result];\n' % nextMethod)


            else:
                file.write('double result = vaule %s %s;\n' % (operator, number))
                print("运算完毕")

        file.write('\nreturn result;\n')

        file.write('\n}\n\n')
    file.write("@end")
    file.close()





def makeNoRepeatClassFile(classFileArr,classCount):
    for k in range(0,classCount):
        className = random.choice(array)
        count = len(classFileArr)

        if count == 0:
            classFileArr.append(className)
        else:
            isDuplicate = 0
            for m in classFileArr:
                if m == className:
                    print("已有该类名，不用重复创建")
                    isDuplicate = 1
                    break

            if isDuplicate == 0:
                classFileArr.append(className)

    return  classFileArr;

def startup():
    createNameArr()
    classFileArr = []
    classPropertyArr = []
    classMethodArr = []

    while len(classFileArr) < defaultNewClassCount:
        n = defaultNewClassCount - len(classFileArr)
        print("还不符合创建类的个数，继续创建 %s 个类文件" % n)
        classFileArr = makeNoRepeatClassFile(classFileArr,n)




    for j in range(0,len(classFileArr)):
        # className = random.choice(array)
        # classFileArr.append(className)
        propryArray = createPropertArr();
        methodArray = createMethodArr();

        classPropertyArr.append(propryArray);
        classMethodArr.append(methodArray);


    newClassCount = len(classFileArr);




    for i in range(0,newClassCount):
        className = classFileArr[i];
        thisprop = classPropertyArr[i];
        thismethod = classMethodArr[i];


        nextClassName = ""
        nextMethod = ""
        if i + 1 < newClassCount:
            nextClassName = classFileArr[i + 1];
            nextMethodArr = classMethodArr[i + 1];
            nextMethod = nextMethodArr[0]

            # print('创建类 classanme=%s index = %s' % (className,i) )


        else:
            print("没有下一个类了,当前类index = %s" % i)


        firstclass = 0;
        if i == 0:
            firstclass = 1;


        # createMethodArr();
        createFileH(projectPath, defaultProjectName, className, nextClassName, thisprop, thismethod,firstclass)
        createFileM(projectPath, defaultProjectName, className, nextClassName, thisprop, thismethod,nextMethod)






if __name__ == '__main__':
    startup()






