# TOPSY_Automation_fMRS_Pipeline
This is the official documentation for the TOPSY Automated fMRS Pipeline, automated in Python using SikuliX IDE.



## Installation
1. This pipeline requires the download of a couple pieces of free software. 

<ul>
<li>Firstly, the automation software we are using depends on SikuliX IDE, which in turn relies on Java. Download Java and follow instructions for installation <a href="https://www.java.com/en/">here</a>. Download SikuliX IDE <a href="https://raiman.github.io/SikuliX1/downloads.html">here<a>. It should download as a .jar file, which you should move to an easily locatable folder, such as your "Desktop" or "Documents" folder. For the rest of this documentation, we'll assume you moved it to your desktop folder.  </li>
  
<li>You need Python to run this automation pipeline. You can download Python <a href="https://www.python.org/downloads/">here</a>.</li>

 <li> For the fMRS analysis, it's important for you to have both fitMAN and BARSTOOL downloaded and working successfully on your computer. For more information on how to download and run these, click <a href="https://github.com/dwong263/MAGIQ/wiki/Installation-Overview">here</a>. </li>
  
 <li> You also need to have Visual Studio Code downloaded. It can be downloaded <a href="https://code.visualstudio.com/download">here</a>. </li>
  
  <li> You also need Hyper terminal to be downloaded. Download <a href="https://hyper.is/">here</a>
  
 <li> Finally, scroll up, click on the green button that says "Code" and download this repository. Inside you should find a folder called PipelineFull.sikuli </li>
  
  </ul>
  
  <br/>
    <br/>
    <br/>
    <br/>

  2. Once you have downloaded all the required pieces of software, open your terminal app. If you don't know how to do this, follow instructions directly below.
  
  <ul>
<li> On Mac, Go to Finder -> Applications -> Utilities -> Terminal and open terminal. </li>
    <li> On Windows, follow <a href="https://www.wikihow.com/Open-Terminal-in-Windows">these</a> instructions </li>
  </ul>
  
<br/>
<br/>
<br/>
<br/>
  
  
  3. You need to use terminal to open SikuliX IDE, otherwise it won't work (you can't just double click on the .jar file).
  - In the command prompt, write the following command and then hit enter: cd Desktop
  - Now write the following command and hit enter: java -jar sikulixide-2.0.5.jar
  
<br/>
<br/>
<br/>
<br/>
  
  
  4. SikuliX may request access to various functionalities on your computer, go to your system preferences and allow it access based on its instructions. 
  
<br/>
<br/>
<br/>
<br/>
  
  
  5. Once the SikuliX IDE has opened, should look something like this: 
  
  <img src="https://i.ibb.co/47Qrw8f/Screen-Shot-2021-12-06-at-11-50-35-AM.png" style="width:700px"/>
            
Click on File --> Open. Now navigate to the folder where you downloaded this repository, most likely your "Downloads" folder. Open PipelineFull.sikuli. Scroll all the way down through the files in this folder and at the bottom, double click PipelineFull.py. You should see this window now: 
  
  
  <img width="700" alt="Screen Shot 2021-12-06 at 12 01 04 PM" src="https://user-images.githubusercontent.com/50881444/144889170-7b0d7e3f-6d64-49c5-8aa2-7d611f6b2015.png">
  
Before you run the code, we need to open Hyper terminal now. 
  
  
  6. Open Hyper terminal by clicking on it in your Applications folder. Now, wherever you downloaded your MAGIQ folder from the fitMAN and BARSTOOL installation process, we need to navigate there using Hyper. Supposing that MAGIQ folder is simply in your Downloads folder, we can do this in the Hyper command prompt:
  
  - type the following and then hit enter: cd Downloads 
  - type the following and then hit enter: cd MAGIQ-0.3-beta 

7. Your fMRS dataset should be named appropiately according to the subject ID and the acquisition date, for example: 
  
  <img width="769" alt="Screen Shot 2021-12-06 at 12 09 23 PM" src="https://user-images.githubusercontent.com/50881444/144890438-61b7e3b2-01fb-423b-aeae-601e1380850d.png">
  
  
  
    
8.  Now you are all good to go, go back to SikuliX IDE window and hit run in the top right hand corner of the window.
  
  <img width="174" alt="Screen Shot 2021-12-06 at 12 10 27 PM" src="https://user-images.githubusercontent.com/50881444/144890579-e31618db-5b80-4c18-a8bf-4e2df2badaf9.png">


<img width="200" alt="Screen Shot 2021-12-06 at 12 07 54 PM" src="https://user-images.githubusercontent.com/50881444/144890186-9e35788f-1ff6-4e73-b4f2-ff3634389a45.png">
  

