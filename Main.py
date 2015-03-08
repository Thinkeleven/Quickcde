#PyCalc
func = ['var','console.log','if','else']
operations = ['*','/','+','-']
iffunc = ['==','<','>','!=']
import os
#Parser
#def Parse(sys.argv[1]):

def wolfram_alpha(speech):
    import urllib.request
    import json
    from xml.etree import ElementTree
    import time
    done = False
    url_section = urllib.parse.urlencode(dict(input=speech, appid="26758T-QTK4RYKH8U",))
    url = 'http://api.wolframalpha.com/v2/query?' + url_section
    response = urllib.request.urlopen(url)

    tree = ElementTree.parse(response)
    root = tree.getroot()

    for node in root.findall('.//pod'):
        if node == '':
            print('Sorry, Wolfram|Alpha could not understand your query \''+speech+'. Please try again.')

        else:
            print(node.attrib['title'])
            for text_node in node.findall('.//plaintext'):
                if text_node.text:
                    print(text_node.text)
            print("****")
    p = input('Press \'ENTER\' to continue with code')
    os.system('cls')


def runWA(query):
    #print('WOLFRAM|ALPHA!')
    wolfram_alpha_app_id = "26758T-QTK4RYKH8U"
    speech = query
    wolfram_alpha(speech)







#REQUIRED FUNCTIONS!!!!!
#____________________________
def Parse(mathCalc):
    parsed_tmp1 = mathCalc.split(';')
    parsed_tmp2 = []
    global func,operations,iffunc
    for p in parsed_tmp1:
        i = ''
        countvalue = False
        for m in p:
            if m == ';':
                countvalue = True
            else:
                i = i+str(m)
        if countvalue == False:
            #print('STE')
            pass
        sp_1 = i.split()
        #print(sp_1)
        parsed_tmp2.append(sp_1)
    return parsed_tmp2


def Compile(mathCalc):
    #print('a',mathCalc)
    totalcode = 'import time\nimport os\n'
    for i in mathCalc:
        #print('h',i)
        #print('nope')
        firstcode = ''
        if i[0] == 'var':
            del i[0]
            i.insert(1,'=')
            firstcode = ''
            for api in i:
                firstcode = firstcode+str(api)
                #print('sorry to spam you')
            #print('done')
        #print('1')
        if i[0] == 'console.log':
            #print('CONSOLE.LOG')
            i[0] = 'print('
            i.append(')')
            firstcode = ''
            for api in i:
                firstcode = firstcode+str(api)
            totalcode = firstcode
            print(firstcode)
            #print('done')
        #print('2')
        #if i[0] == 'pymath':
            #del i[0]
            #firstcode = ''
            #for api in i:
              #  firstcode = firstcode+str(api)
        #print('3')
        if i[0] == 'pycode{':
            del i[0]
            #print('PYCODE!')
            apiTMPbool = False
            #print(i)
            try:
                i.remove('}')
            except ValueError:
                raise SyntaxError('Missing parameter when working...')
            firstcode = ''
            for api in i:
                firstcode = firstcode+str(api)
        else:
            #print('4')
            pass
        if i[0] == 'query':
            restxt = ''
            #print('query')
            del(i[0])
            reslst = i
            numtmp = len(i)
            for i in range(1,numtmp-1):
                reslst.insert(i,' ')
            for i in reslst:
                restxt = restxt+str(i)
            #print(restxt)
            runWA(restxt)
        if i[0] == 'system':
            #print('system')
            i[0] = '\nos.system(\''
            i.append('\')\n')
            for m in i:
                totalcode = totalcode+str(m)
        if i[0] == 'time':
            #print('system')
            i[0] = '\ntime.'
            for m in i:
                totalcode = totalcode+str(m)


        totalcode = totalcode+'\n'
        totalcode = totalcode+firstcode
    totalrcode = 'import time\nimport os\n' + totalcode
    #print('TOTALCODE...\n\n******************************')
    totalcode = totalrcode
    #print(totalcode)
    exec(totalcode)

#animate_function('ABCDEFG!')

while True:
    ste = Parse(input('Code?\n'))
    Compile(ste)

