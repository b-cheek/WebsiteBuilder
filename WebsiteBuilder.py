## This is Website Builder, a python tool that can be used to help create HTML websites in a simple way

##importing the required libraries to run the program
import os
import webbrowser as wb
from tkinter import *
from tkinter.colorchooser import askcolor              

#setting values to 0 before the main code begins
sitesNum = 0

def sitesDisplay():
##  displays all html files in the directory of the program for the user to reference when viewing or deleting files
    #creating the lists that will be used in the viewing portion
    sitesNum = 0
    dirFiles=[]
    dirSites=[]
    for root, dirs, files in os.walk("."):
            for filename in files:
                    dirFiles.append(filename)
    for i in dirFiles:
            if i[-5:]=='.html':
                    dirSites.append(i)

    print ('')      
    for i in dirSites:
            print (i)
            sitesNum+=1
    print(sitesNum)

print ("-----------------------------------")
print ("    WELCOME TO WEBSITE BUILDER!  ")
print ("-----------------------------------")
print ('')

##this is to prevent unnecessary clutter in your files and reduce stress on the program as you manage your files
print ("If this is your first time using Website Builder, we recommend that you move the Website Builder program into its own file. This helps in the organization and management of the files that you will create")

##this first loop is so the user can return to the homepage from the viewing portion
websiteBuilder=True
while websiteBuilder==True:
##      this loop allows the user to return to the homepage after creating a website
        createLoop=True
        while createLoop==True:
##              shows sites the user has created
                print ('')
                print ('Sites you have created:')
                sitesDisplay()
##              These values are set to false unless the user chooses to customize the background
                cBack=False
                iBack=False
                print ('')
##              this first question is to determine whether the user goes to the website creating portion or the viewing portion
                create=str(input("Would you like to create a website? "))
                
                if create.lower()=='yes':
##                      getting the file name for the website and the name displayed in the tab
##                      the information is then formatted to fit HTML
                        print('')
                        fileName=str(input("What would would you like the file to be named? "))
                        fileName=(fileName+".html")
                        print ('')
                        
                        name=str(input("What is the name of your website? "))
                        siteHtml=('<title>'+(name)+'</title>')
                        
                        print ('')
##                      asks if the user would like to use a template or make their own website from scratch
                        custom=str(input("Would you like to use a template? "))
                        if custom.lower()=='no':
##                              setting up the while loop to add individual elements that will occur later
                                creating=True
                                print ('')
##                              setting up the background before individual elements are added
                                backG=str(input("Would you like customize your background? "))
                                print ('')
                                if backG.lower()=='yes':
##                                      allowing the user to select a color or image to be the background, and formatting their choice of color or image into HTML
                                        backChoice=str(input("Would you like your background to be a color or an image (the image will repeat based on its size)? "))
                                        print ('')
                                        if backChoice.lower()=='color':
                                                cBack=True
                                                print ("The color choosing page is on your desktop")
                                                print ("It is recommended to ignore the other dialogue box, it will close when the program ends")
                                                print ('')
                                                bkgColor=askcolor()
                                                bkgColor=bkgColor[1]
                                        elif backChoice.lower()=='image':
                                                iBack=True
                                                bkgImage=str(input("Please input the URL of the image "))
                                                
##                      Lines 75 to 117 were created by my partner        
                        elif custom.lower()=='yes':
                                siteHtml=''
                                print("TEMPLATES:\n")
                                print("1:Header, image, and text")
                                print("2:Large header with 2 subsections")

                                templateChoice=str(input("Choose the number of the template you would like to use: "))
                                if templateChoice=="1":
                                        header=str(input("Enter the text for the header: "))
                                        image=''
                                        print("Enter \"my own\" to use your own image")
                                        imageType=str(input("or enter \"url\" to use an image from the internet "))
                                        if imageType.lower()=='my own':
                                                print ("Make sure that the image is in the same file as this program")
                                                image=str(input("Paste the file name of the image here: "))
                                                print ('')
                                                
                                        if imageType.lower()=='url':
                                                image=str(input("Please input the URL of the image "))
                                                print ('')
                                        text=str(input("Enter the text for the website"))
                                        siteHtml=((siteHtml)+"<html><head><title>"+(name)+"</title></head><body><h1>"+(header)+"</h1><hr/><img src=\""+(image)+"\"><p>"+(text)+"</p></body></html>")

                                        f = open(fileName,'w')
                                        f.write(str(siteHtml))
                                        f.close()
                                        print("Opening website...")
                                        wb.open_new_tab(fileName)

                                if templateChoice=="2":
                                        topHeader=str(input("Enter the text for the top header: "))
                                        header1=str(input("Enter the text for the first subheading: "))
                                        text1=str(input("Enter the text for the first subtext: "))
                                        header2=str(input("Enter the text for the second subheading: "))
                                        text2=str(input("Enter the text for the second subtext: "))

                                        siteHtml=((siteHtml)+"<html><head><title>"+(name)+"</title></head><body><h1>"+(topHeader)+"</h1><hr/><h3>"+(header1)+"</h3><p>"+(text1)+"</p><hr/><h3>"+(header2)+"</h3><p>"+(text2)+"</p></body></html>")
                                        f = open(fileName,'w')
                                        f.write(str(siteHtml))
                                        f.close()
                                        print("Opening website...")
                                        wb.open_new_tab(fileName)
                                creating=False
##                              Code that I created resumes

##                      the loop that is used to continuously add elements
                        while creating==True:

##                              creating a standard description of elements to add and how to finish creation after each element is added
                                print ("Enter \"finish\" to create the website")
                                print ("What element would you like to add? ")
                                print ("\"header\", \"text\", \"image\", or \"horizontal line\" (\"hl\")")
                                element=str(input(''))
                                print ('')
                                
##                              ending the loop to add elements, writing the html script, and opening the website in a web browser
                                if element.lower()=='finish':
                                    creating=False
                                    if cBack==True:
                                            siteHtml=('<body bgcolor="'+(bkgColor)+'">'+(siteHtml)+'</body>')

                                    elif iBack==True:
                                            siteHtml=('<body background="'+(bkgImage)+'">'+(siteHtml)+'</body>')
                                            
                                    f = open(fileName,'w')

                                    f.write(siteHtml)
                                    f.close()

                                    wb.open_new_tab(fileName)
                                    
##                              creating the header element
                                elif element.lower()=='header':
                                        header=str(input("Enter the text for the the header: "))
                                        print ('')
##                                      customization for the header, and reminding the user of the background if applicable
                                        if backG.lower()=='yes':
                                                print ("note how the color of your header will look with your background")
                                        custom=str(input("Would you like to customize this element? "))
                                        
                                        print ('')
                                        
                                        if custom.lower()=='yes':
                                                customChoice=str(input("would you like to customize color, position (default is left), or both? "))
                                                print ('')

##                                              custom color selection
                                                if customChoice.lower()=='color':
                                                         print ("The color choosing page is on your desktop")
                                                         print ("It is recommended to ignore the other dialogue box")
                                                         print ('')
##                                                       asking the user to select a color using a dialogue box and formatting the answer into HTML
                                                         color=askcolor()
                                                         color=color[1]
                                                         siteHtml=((siteHtml)+'<h1 style="color:'+(color)+'">'+(header)+'</h1>')
                                                         
##                                              custom position and HTML formatting
                                                elif customChoice.lower()=='position':
                                                        alignment=str(input("Would you like to align the header to the right or center? "))
##                                                      formatting the position into HTML
                                                        if alignment=='right':
                                                                siteHtml=((siteHtml)+'<h1 align="right">'+(header)+'</h1>')
                                                        if alignment=='center':
                                                                siteHtml=((siteHtml)+'<h1 align="center">'+(header)+'</h1>')
                                                        print ('')

##                                              if the user wants to do both custom color and position
                                                elif customChoice.lower()=='both':
                                                        print ("The color choosing page is on your desktop")
                                                        print ("It is recommended to ignore the other dialogue box")
                                                        print ('')
                                                        color=askcolor()
                                                        color=color[1]
##                                                      formatting for both color and position
                                                        alignment=str(input("Would you like to align the header to the right or center? "))
                                                        if alignment=='right':
                                                                siteHtml=((siteHtml)+'<h1 style="color:'+(color)+'" align="right">'+(header)+'</h1>')
                                                        if alignment=='center':
                                                                siteHtml=((siteHtml)+'<h1 style="color:'+(color)+'" align="center">'+(header)+'</h1>')
                                                        print ('')

                                                else:
                                                        print ("Please input a valid answer")
                                                        print ("(The element has been deleted)")
                                                        
##                                      for the default form of the element
                                        elif custom.lower()=='no':
                                                siteHtml=((siteHtml)+"<h1>"+(header)+"</h1>")
                                                         

                                        
                                        print ('')
##                                creating the image element
                                elif element.lower()=='image':
##                                      asking the user where they want to source their image from
                                        print("Enter \"my own\" to use your own image")
                                        imageType=str(input("or enter \"url\" to use an image from the internet "))
                                        if imageType.lower()=='my own':
##                                              The image has to be in the same directory for the program to find it
                                                print ("Make sure that the image is in the same file as this program")
                                                image=str(input("Paste the file name of the image here: "))
                                                print ('')
##                                              custom alignment options
                                                align=str(input("Would you like to align the image (default is left)? "))
                                                if align.lower()=='yes':
                                                        print ('')
                                                        alignImg=str(input("Would you like to align the image to right or center? "))
##                                                      formatting the image into the HTML
                                                        if alignImg.lower()=='right':
                                                                siteHtml=((siteHtml)+'<img src=\"'+(image)+'\" align="right"></img>')
                                                        if alignImg.lower()=='center':
                                                                siteHtml=((siteHtml)+'<center><img src=\"'+(image)+'\"></img></center>')
                                                        print ('')

                                                

                                                else:
                                                        print ('')
##                                                      formatting the image into the HTML
                                                        siteHtml=((siteHtml)+'<img src=\"'+(image)+'\"></img>')
                                                                        
##                                      for if the user wants to use an image from the internet        
                                        elif imageType.lower()=='url':
                                                print ('')
                                                image=str(input("Please input the URL of the image "))
                                                print ('')
##                                              custom alignment options
                                                align=str(input("Would you like to align the image (default is left)? "))
                                                if align.lower()=='yes':
                                                        print ('')
                                                        alignImg=str(input("Would you like to align the image to right or center? "))
##                                                      formatting the image into the HTML
                                                        if alignImg.lower()=='right':
                                                                siteHtml=((siteHtml)+'<img src=\"'+(image)+'\" align="right"></img>')
                                                        if alignImg.lower()=='center':
                                                                siteHtml=((siteHtml)+'<center><img src=\"'+(image)+'\"></img></center>')
                                                        print ('')

                                                else:
                                                        print ('')
##                                                      formatting the image into the HTML
                                                        siteHtml=((siteHtml)+'<img src=\"'+(image)+'\"></img>')
                                        
##                              creating the text element
                                elif element.lower()=='text':
                                        text=str(input("Enter the text: "))
                                        print ('')
##                                      customization for the text, and reminding the user of the background if applicable
                                        if backG.lower()=='yes':
                                                print ("note how the color of your header will look with your background")
                                        custom=str(input("Would you like to customize this element? "))
                                        print ('')
                                        
                                        if custom.lower()=='yes':
                                                customChoice=str(input("would you like to customize color, position, or both? "))
##                                              custom color selection
                                                if customChoice.lower()=='color':
##                                                       asking the user to select a color using a dialogue box and formatting the answer into HTML
                                                         print ("The color choosing page is on your desktop")
                                                         print ("It is recommended to ignore the other dialogue box")
                                                         color=askcolor()
                                                         color=color[1]
                                                         siteHtml=((siteHtml)+'<p style="color:'+(color)+'">'+(text)+'</p>')

##                                              custom alignment options         
                                                elif customChoice.lower()=='position':
                                                        alignment=str(input("Would you like to align the header to the right or center? "))
##                                                      formatting the aligned text into HTML
                                                        if alignment=='right':
                                                                siteHtml=((siteHtml)+'<h1 align="right">'+(header)+'</h1>')
                                                        if alignment=='center':
                                                                siteHtml=((siteHtml)+'<h1 align="center">'+(header)+'</h1>')
                                                        print ('')

##                                              if the user wants to do both custom color and position        
                                                elif customChoice.lower()=='both':      
                                                        print ("The color choosing page is on your desktop")
                                                        print ("It is recommended to ignore the other dialogue box")
                                                        print ('')
                                                        color=askcolor()
                                                        color=color[1]
                                                        alignment=str(input("Would you like to align the text to the right or center? "))
##                                                      formatting both color and position into HTML
                                                        if alignment=='right':
                                                                siteHtml=((siteHtml)+'<p style="color:'+(color)+'" align="right">'+(text)+'</p>')
                                                        if alignment=='center':
                                                                siteHtml=((siteHtml)+'<p style="color:'+(color)+'" align="center">'+(text)+'</p>')
                                                        print ('')
##                                      for default color and position
                                        if custom.lower()=='no':
                                                siteHtml=((siteHtml)+"<p>"+(text)+"</p>")
                                        print ('')

##                              creating the horizontal rule element
                                elif element.lower()=='horizontal line' or element.lower()=='hl':
                                        customChoice=str(input("Would you like to color this element? "))
                                        print ('')

##                                      custom color selection
                                        if customChoice.lower()=='yes':
                                                print ("The color choosing page is on your desktop")
                                                print ("It is recommended to ignore the other dialogue box, it will close when the program ends")
                                                print ('')
                                                color=askcolor()
                                                color=color[1]
                                                siteHtml=((siteHtml)+'<hr color="'+(color)+'"></hr>')

                                        if customChoice.lower()=='no':
                                                siteHtml=((siteHtml)+"<hr></hr>")

##                              informing the user if they mistype the response
                                else:
                                        print ("Please input a valid answer")
                                        print ('')
                                                
##                      finishing the element adding process
                        createLoop=False

##              Website viewing screen, this is also the portion used to end the program
                elif create.lower()=='no':
##                  loop that allows the user to end the program after deleting files
                    viewLoop=True
                    while viewLoop==True:
                            print ('')
##                          Gives options for if the user wishes to view or delete files, create a website, or end the program
                            otherOptions=str(input("Input \"view\" to view and delete files, \"finish\" to go back to the homepage, or \"end\" to end the program. "))
                            if otherOptions=='view':
                                    sitesDisplay()

                                    if sitesNum>0:
                                            print ('')
                                            print ("You have created",(sitesNum),"websites")
                                            createLoop=False

##                                  option for if no websites have been created, redirects the user to create a website   
                                    else:
                                            print ("You have not created any websites")
                                            viewLoop=False
                                            
                                    
                                    if createLoop==False:
##                                          gives the user options for what they wish to do with the websites that they have created
                                            print ("What would you like to do with your files?")
                                            print ("(\"view\", \"edit\", \"delete\", or \"delete all\")")
                                            viewChoice=str(input(""))
                                            print ('')

##                                          option to delete websites
                                            if viewChoice.lower()=='delete':
                                                           deleting=True
##                                                         loop allows the user to delete multiple specific websites
                                                           while deleting==True:
                                                                   print ('')
                                                                   print("enter \"finish\" to stop deleting")
                                                                   deleteChoice=str(input("Enter the name of the file you would like to delete "))
                                                                   if deleteChoice.lower()=='finish':
                                                                           deleting=False
##                                                                 allows the user to delete a non-html file if they wish, but warns them
                                                                   elif deleteChoice[-5:]!='.html':
                                                                           deleteSure=str(input("Are you sure you want to delete this? This is not an HTML file"))
                                                                           if deleteSure.lower()=='yes':
                                                                               os.remove(deleteChoice)

                                                                   else:
##                                                                         deletes the selected website and informs the user
                                                                           os.remove(deleteChoice)
                                                                           print((deleteChoice),"has been deleted")
                                                                   
##                                          gives the option to delete all existing html files in the directory of the program
                                            elif viewChoice.lower()=='delete all':
##                                                  a final confirmation before all of the html files are deleted
                                                    deleteSure=str(input("Are you sure? "))
                                                    print ('')
                                                    
                                                    if deleteSure.lower()=='yes':
                                                            for i in dirSites:
                                                                    os.remove(i)
                                                            print ("All of your websites have been deleted")

                                                    elif deleteSure.lower()=='no':
                                                            viewLoop=False

                                            elif viewChoice.lower()=='view':
                                                    viewing=True
##                                                  allows the viewer to view multiple websites they have created
                                                    while viewing==True:
                                                            print ('')
                                                            print ("enter \"finish\" to stop viewing")
                                                            fileView=str(input("Enter the name of the file you would like to view "))
                                                            if fileView.lower()=='finish':
                                                                    viewing=False
                                                            else:
                                                                    f=open(fileView)
                                                                    wb.open_new_tab(fileView)
                                                                    f.close
                                                                    
##                          ends the loop, bringing the user back into the "createLoop" loop
                            elif otherOptions=='finish':
                                    viewLoop=False

##                          ends the program entirely
                            elif otherOptions=='end':
                                    websiteBuilder=False
                                    createLoop=False
                                    viewLoop=False
                
##              gives the user feedback in the event of a misinput                          
                else:
                        
                        print("Please input a valid answer (yes or no)")