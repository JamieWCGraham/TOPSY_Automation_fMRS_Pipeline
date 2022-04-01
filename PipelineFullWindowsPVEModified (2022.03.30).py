import time
from sikuli import *


def TicTocGenerator():
    # Generator that returns time differences
    ti = 0           # initial time
    tf = time.time() # final time
    while True:
        ti = tf
        tf = time.time()
        yield tf-ti # returns the time difference

TicToc = TicTocGenerator() # create an instance of the TicTocGen generator

# This will be the main function through which we define both tic() and toc()
def toc(tempBool=True):
    # Prints the time difference yielded by generator instance TicToc
    tempTimeInterval = next(TicToc)
    if tempBool:
        print( "Elapsed time: %f seconds.\n" %tempTimeInterval )

def tic():
    # Records a time in TicToc, marks the beginning of a time interval
    toc(False)

tic()



# START OF AUTOMATION CODE!! 

# This is an automation code that seeks to automate the fMRS pipeline for Dr. Palaniyappan's Lab.


# Adjust settings
Settings.MoveMouseDelay = 0.1
Settings.TypeDelay = 0

# User input prompts 

num_of_spec = int(input("# of spectra?"))
date = int(input("year/date of acquisition (YYYYMMDD)"))
id = int(input("subject ID"))
global flawed
flawed = str(input("flawed dataset (Y or N)? (voxel positioning bug)"))
inner_re_edit = "N"    # don't worry about this, just an initialization of a parameter we'll need later
#slide_length = int(input("slider_length: "))
slide_length = 128/num_of_spec
#slide_block = int(input("slide or block averaging (1 or 0) ?: "))
slide_block = 0
dataType = int(input("HC,FEP,Chr, PRO(CHR)? (input 1,2,3, or 4 respectively) :"))

if dataType==1:
    global dataEnd
    dataEnd = ".HC"
elif dataType==2:
    global dataEnd
    dataEnd = ".FEP"
elif dataType==3:
    global dataEnd
    dataEnd = ".Chr"
else:
    global dataEnd
    dataEnd = ".PRO(CHR)"

global h
h = "C:/Users/peter/Desktop/Sikuli/Sikuli/PipelineFullWindows.sikuli2/"

global screen
screen = Screen(1)

global edit
edit="N"     # here we are initializing an important variable, this accounts for whether we have adjusted for voxel positioning or not.

if id <= 99:
    file_title = "TOPSY0" +  str(id) + "_" + str(date)
else:
    file_title = "TOPSY" +  str(id) + "_" + str(date)





# here we need to change this part of the code to the pathway for our spectra datasets" 

file_path = "/home/pjeon/Documents/"

# defining some useful automation functions 





      
def waitP(file,thresh,forever):
    if forever:
        screen.wait(Pattern(h + file).similar(thresh),3600)
    else:
        try:
            screen.wait(Pattern(h + file).similar(thresh))
        except:
            screen.wait(Pattern(h + file).similar(thresh),3600)
        

      
def clickP(file,thresh,forever):
    if forever:
        screen.click(Pattern(h + file).similar(thresh),3600)
    else:
        try:
            screen.click(Pattern(h + file).similar(thresh))
        except:
            screen.click(Pattern(h + file).similar(thresh),3600)
            
            
def click2P(file,thresh,forever):
    if forever:
        screen.doubleClick(Pattern(h + file).similar(thresh),3600)
    else:
        try:
            screen.doubleClick(Pattern(h + file).similar(thresh))
        except:
            screen.doubleClick(Pattern(h + file).similar(thresh),3600)
            
            
def click2RP(file,thresh,forever):
    if forever:
        screen.rightClick(Pattern(h + file).similar(thresh),3600)
    else:
        try:
            screen.rightClick(Pattern(h + file).similar(thresh))
        except:
            screen.rightClick(Pattern(h + file).similar(thresh),3600)
            
            
def existsP(file,thresh):
    screen.exists(Pattern(h + file).similar(thresh))


def waitclickP(file,thresh,forever):
    waitP(file,thresh,forever)
    clickP(file,thresh,forever)

def wait2clickP(file,thresh,forever):
    waitP(file,thresh,forever)
    click2P(file,thresh,forever)

def wait2rightclickP(file,thresh,forever):
    waitP(file,thresh,forever)
    click2RP(file,thresh,forever)

def waitclickPTO(file,thresh,forever,x_coord,y_coord):
    waitP(file,thresh,forever)
    if forever:
        screen.click(Pattern(h + file).similar(thresh).targetOffset(x_coord,y_coord),3600)
    else:
        try:
            screen.click(Pattern(h + file).similar(thresh).targetOffset(x_coord,y_coord))
        except:
            screen.click(Pattern(h + file).similar(thresh).targetOffset(x_coord,y_coord),3600)
        
def wait2clickPTO(file,thresh,forever,x_coord,y_coord):
    waitP(file,thresh,forever)
    if forever:
        screen.doubleClick(Pattern(h + file).similar(thresh).targetOffset(x_coord,y_coord),3600)
    else:
        try:
            screen.doubleClick(Pattern(h + file).similar(thresh).targetOffset(x_coord,y_coord))
        except:
            screen.doubleClick(Pattern(h + file).similar(thresh).targetOffset(x_coord,y_coord),3600)




def terminal2():
    type("n", Key.CTRL)
    wait(3)
    wait2rightclickP("MAGIQ.png",0.8,0)
    wait(3)
    waitclickP("OpenT.png",0.8,0)

def terminal():
    screen = Screen(1)
    wait(2)
    type("t",Key.CTRL + Key.ALT)
    wait(3)
    type("cd MAGIQ_6" + Key.ENTER)

def closeNow(): 
    type(Key.F4,Key.ALT)
    type(Key.ENTER)
    type(Key.ENTER)



def flawedSetup():  
    if flawed == "Y":
        global screen
        screen = Screen(0)
        type("r",Key.WIN)
        type(Key.BACKSPACE)
        wait(3)
        type("cmd" + Key.ENTER)
        wait(3)
        paste("matlab/R2021b") 
        type(Key.ENTER)
        
        screen = Screen(0)
        #waitclickP("matlab.png",0.8,1)
        waitclickP("voxel_adjust.png",0.8,1)
        waitclickP("yellow_green_folder.png",0.8,1)
        waitclickP("folder_text_box.png",0.8,1)
        paste("C:\Users\peter\Desktop\Sikuli\Sikuli\ExtractPosition\common\dicom")
        waitclickP("select_folder.png",0.8,1)
        waitclickP("run_green.png",0.8,1)
        wait(2)
        waitclickP("two_arrows.png",0.8,1) 
        type("clipboard(c,coords.dSag)")
        wait(3)
        type(Key.ENTER)
        wait(3)
        flawed_coords_x = round(float(Env.getClipboard()),1)
        wait(3)
        type("clipboard(c,coords.dCor)")
        wait(3)
        type(Key.ENTER)
        wait(3)
        flawed_coords_y = round(float(Env.getClipboard()),1)
        wait(3)
        type("clipboard(c,coords.dTra)")
        wait(3)
        type(Key.ENTER)
        wait(3)
        flawed_coords_z = round(float(Env.getClipboard()),1)
        global flawed_coords
        flawed_coords = [flawed_coords_x, flawed_coords_y, flawed_coords_z]
        global coords_length 
        coords_length = len(str(flawed_coords))-2
        print(coords_length)
        #global screen
        screen = Screen(1)



def voxel_adjust():
    wait2clickPTO("machine.png",0.8,1,0,-30)
    terminal()
    wait(2)
    type("gedit dataclasses.py")
    type(Key.ENTER)
    wait(2)
    type("f", Key.CTRL)
    type("fid_pvec")
    waitclickPTO("sikuli.png",0.71,0,-33,15)
    wait(3)
    type("fid_pvec = np.array(" + str(flawed_coords) + ",'f8')" + " #sikul2")  
    type("s",Key.CTRL)
    type("w",Key.CTRL)
    type("w",Key.CTRL)       
    closeNow() 
    closeNow()
    global edit         
    edit="Y"





    

def voxel_de_adjust():
    wait2clickPTO("machine.png",0.8,1,0,-30)
    terminal()
    wait(3)
    type("gedit dataclasses.py")
    type(Key.ENTER)
    wait(2)
    type("f", Key.CTRL)
    type("fid_pvec")
    waitclickPTO("sikuli2.png",0.71,0,55,0)
    for i in range((36 + coords_length)):
        type(Key.BACKSPACE)
    wait(3)
    type("s",Key.CTRL)
    type("q",Key.CTRL)            
    closeNow()
    global inner_re_edit 
    inner_re_edit = "Y"



def matlabSlidingAverage():
    global screen
    screen = Screen(0)
    #waitclickP("matlab.png",0.8,1)
    waitclickP("input_matlab.png",0.8,1)
    waitclickP("yellow_green_folder.png",0.8,0)
    waitclickP("folder_text_box.png",0.8,1)
    paste("C:\Users\peter\Documents\SpecFit\Correction_Conversion_Combined")
    waitclickP("select_folder.png",0.8,0)
    waitclickP("run_green.png",0.8,0)
    wait(5)
    type(str(id) + Key.ENTER)
    wait(3) 
    type("100" + Key.ENTER)
    wait(3)
    type(str(slide_length) + Key.ENTER)
    wait(3)
    type("128" + Key.ENTER)
    wait(3)
    type(str(num_of_spec) + Key.ENTER)
    wait(3)
    type(str(date) + Key.ENTER)
    wait(3)
    type(str(slide_block) + Key.ENTER)
    waitclickP("select_folder.png",0.8,1)
    waitP("open_matlab.png",0.8,1)
    wait(3)
    type(file_title + "_sup.rda")
    waitclickP("open_matlab.png",0.8,1)
    waitclickP("elapsed_time.png",0.8,1)
    global screen
    screen = Screen(1)
    
    # type(str(num_of_spec) + Key.ENTER)
    

def copyRDAs():
    wait(2)
    waitclickPTO("machine.png",0.8,1,0,-30)
    wait(3)
    type("t",Key.CTRL + Key.ALT)
    RDA_path = "/media/sf_SpecFit/Correction_Conversion_Combined/" 
    wait(2)
    Env.setClipboard("cp -R " + RDA_path + file_title + "_sup.rda " + RDA_path + file_title + "_uns.rda "  + "/media/sf_SpecFit/96Copy/" + file_title)
    type("v",Key.CTRL + Key.SHIFT)
    type(Key.ENTER)
    for i in range(1,(num_of_spec+1)):
        Env.setClipboard("cp -R " + RDA_path + file_title + "_sup_" + str(i) + ".rda " +   "/media/sf_SpecFit/96Copy/" + file_title)
        type("v",Key.CTRL + Key.SHIFT)
        type(Key.ENTER)

    
     


def setUpFolders():
    type("t",Key.CTRL + Key.ALT)
    wait(2)
    type("cd Documents" + Key.ENTER)
    type("mkdir " + file_title + Key.ENTER)
    type("cd " + file_title + Key.ENTER)
    #type("cd test" + Key.ENTER)
    for i in range(1,(num_of_spec+1)):
        type("mkdir " + str(i) + Key.ENTER)
    wait(3)
    pathC = "/media/sf_SpecFit/96Copy/" + file_title + "/"
    for j in range(1,(num_of_spec+1)):
        wait(1)
        Env.setClipboard("cp -R " + pathC + "sLASER_sim_results.ges " + pathC + file_title + "_std_brain_pveseg.nii.gz " + pathC + file_title + "_std_brain_seg.nii.gz " + pathC + file_title + "_std_brain.nii.gz " + pathC + file_title + "_std.nii.gz " + pathC + "sLASER_sim_results_noMM_te100.cst " + pathC + file_title + ".nii.gz " + pathC + file_title + "_sup_" + str(j) + ".rda " + pathC + file_title + "_sup" + ".rda " + pathC + file_title + "_uns.rda " + pathC +"water.cst " + pathC + "water.ges " + file_path + file_title + "/" + str(j) + "/")
        type("v",Key.CTRL + Key.SHIFT)
        wait(1)
        type(Key.ENTER)
    wait(3)


                    


        # just a little logic here for file naming, we want a leading 0 for ID's less than 100. (e.g TOPSY079) for id 79)
    

def generateNifti():
    global screen
    screen = Screen(0)
    type("r",Key.WIN)
    type(Key.BACKSPACE)
    wait(3)
    type("cmd" + Key.ENTER)
    wait(3)
    paste("matlab/R2021b") 
    type(Key.ENTER)
    waitclickP("dicm2nii.png",0.7,1)
    wait(3)
    waitclickP("yellow_green_folder.png",0.8,0)
    waitclickP("folder_text_box.png",0.8,1)
    paste("C:\Users\peter\Documents\SpecFit\Correction_Conversion_Combined")
    wait(3)
    waitclickP("select_folder.png",0.8,0)
    waitclickP("run_green.png",0.8,0)
    waitclickP("folder.png",0.8,0)
    waitclickP("folder_text_box.png",0.8,1)
    paste("C:\Users\peter\Documents\SpecFit\DATA\Raw" + "\\" + file_title + dataEnd)
    waitclickP("select_folder.png",0.8,0)
    waitclickP("result_folder.png",0.8,0)
    waitclickP("folder_text_box.png",0.8,1)
    type("C:\Users\peter\Documents\SpecFit\DATA\NIFTI")
    waitclickP("select_folder.png",0.8,0)
    waitclickP("start_conversion.png",0.8,0)
    waitclickP("elapsed_time.png",0.7,1)
    global screen
    screen = Screen(1)

def copyNifti():
    screen = Screen(1)
    wait2clickP("Oracle.png",0.7,1) 
    wait(3)
    type("t",Key.CTRL + Key.ALT)
    NIFTI_path = "/media/sf_SpecFit/DATA/NIFTI/" 
    wait(2)
    Env.setClipboard("mv " + NIFTI_path + "mp2rage_sag_750iso_p3_944_UNI_DEN.nii.gz " + NIFTI_path + file_title + ".nii.gz")
    type("v",Key.CTRL + Key.SHIFT)
    type(Key.ENTER)
    wait(3)
    Env.setClipboard("cp -R " +  NIFTI_path + file_title + ".nii.gz " + "/media/sf_SpecFit/96Copy/" + file_title + "/")
    type("v",Key.CTRL + Key.SHIFT)
    type(Key.ENTER)
    wait(3)
    Env.setClipboard("mv " + NIFTI_path + "mp2rage_sag_750iso_p3_UNI_Images.nii.gz " + NIFTI_path + file_title + ".nii.gz")
    type("v",Key.CTRL + Key.SHIFT)
    type(Key.ENTER)
    wait(3)
    Env.setClipboard("cp -R " +  NIFTI_path + file_title + ".nii.gz " + "/media/sf_SpecFit/96Copy/" + file_title + "/")
    type("v",Key.CTRL + Key.SHIFT)
    type(Key.ENTER)


# preprocessing

#generateNifti()
#copyNifti()
screen = Screen(0)
if flawed == "Y":
    flawedSetup()
screen = Screen(1)
if flawed=="Y":
    voxel_adjust()
screen = Screen(0)
matlabSlidingAverage()
copyRDAs()
setUpFolders()



screen = Screen(1)
# this iterates over all 96 spectra and automatically carries out the fitman and barstool protocol for each
try: 
    
    screen = Screen(1)
    # this iterates over all 96 spectra and automatically carries out the fitman and barstool protocol for each


    # FITMAN 3 STEPS (CONVERT, WATER REMOVAL, FITTING)
    #CONVERT
    wait(3)
    waitclickP("Oracle.png",0.7,0)
    terminal()

    # CONVERSION

    for spec_num in range(1,(num_of_spec + 1)):
        wait(1)
        Env.setClipboard("./fitman/bin/Linux/sim2fitman -ow " + file_path + file_title +  "/" + str(spec_num) + "/" + file_title + "_sup_"+ str(spec_num) + ".rda" + " -scale -bc -if -quecc  400  0.000 " + file_path + file_title +  "/" + str(spec_num) + "/" + file_title + "_uns.rda" + " -norm -rscale -rbc -rif " + file_path + file_title +  "/" + str(spec_num) + "/" + file_title + "_" + str(spec_num) )
        type("v",Key.CTRL + Key.SHIFT)
        wait(1)
        type(Key.ENTER)
        wait(1)
        type("1" + Key.ENTER)
        wait(1)
        type("1" + Key.ENTER)
        wait(1)

        
    # WATER REMOVAL

    terminal()
    type(Key.ENTER)
    type(" python" + Key.SPACE + "fitman.py")
    type(Key.ENTER)
    waitclickP("Ok.png",0.77,0)
    waitclickP("Ok.png",0.77,0)
    wait(3)
    waitclickP("options.png",0.71,0)
    wait(3)
    waitclickP("set_default_dir.png",0.71,0)
    wait(3)
    waitclickP("browse.png",0.81,1)
    wait2clickPTO("text-box.png",0.73,1,0,0)

    type(Key.BACKSPACE)

    type(file_path + file_title + "/")

    type(Key.ENTER)

    waitclickP("Ok2.png",0.8,0)


    for spec_num in range(1,(num_of_spec + 1)):
            waitclickP("File.png",0.81,0)
            waitclickP("Data.png",0.78,0)
            waitclickPTO("Directories.png",0.83,0,5,9)
            wait2clickP("text-box.png",0.75,0)
            type(file_path + file_title +  "/" + str(spec_num) + "/" + file_title + "_" + str(spec_num) + "_s.dat" + Key.ENTER)
            waitclickP("Arithmetic.png",0.75,0)
            waitclickP("hsvd_water_removal.png",0.76,0)
            waitclickP("Ok2.png",0.74,0)
            waitclickP("File.png",0.81,0)
            waitclickP("save_active_window.png",0.81,0)
            waitclickPTO("Directories.png",0.83,0,5,9)
            wait2clickP("text-box.png",0.8,0)
            type(file_path + file_title +  "/" + str(spec_num) + "/" + file_title + "_sup.dat")
            type(Key.ENTER)
            

    # FITTING
    terminal()
    for spec_num in range(1,(num_of_spec + 1)):
        wait(3)
        Env.setClipboard("./fitman/bin/ultra_fitman " + file_path + file_title +  "/" + str(spec_num) + "/" + file_title + "_sup.dat " + file_path + file_title +  "/" + str(spec_num) + "/" + "sLASER_sim_results.ges " + file_path + file_title +  "/" + str(spec_num) + "/" + "sLASER_sim_results_noMM_te100.cst " + file_path + file_title +  "/" + str(spec_num) + "/" + file_title +  "_sup.out")
        type("v",Key.CTRL + Key.SHIFT)
        wait(1)
        type(Key.ENTER)
        waitP("fit_completed.png",0.8,0)
    for spec_num in range(1,(num_of_spec + 1)):
        wait(3)
        Env.setClipboard("./fitman/bin/ultra_fitman " + file_path + file_title +  "/" + str(spec_num) + "/" + file_title + "_" + str(spec_num)  + "_uns.dat " + file_path + file_title +  "/" + str(spec_num) + "/" + "water.ges " + file_path + file_title +  "/" + str(spec_num) + "/" + "water.cst " + file_path + file_title +  "/" + str(spec_num) + "/" + file_title + "_uns.out")
        type("v",Key.CTRL + Key.SHIFT)
        wait(1)
        type(Key.ENTER)
        waitP("fit_completed.png",0.8,0)
        

        
        
    
    for spec_num in range(1,(num_of_spec + 1)):
        tic()
        # BARSTOOL NOW!!! 

        closeNow()

        wait(3)
        terminal()
    
        waitclickP("white_square.png",0.8,0)
        type("python" + Key.SPACE + "barstool.py")
        type(Key.ENTER)
        
        
        wait(3)
    
        waitclickP("set_working_directory.png",0.8,1)
        
                
        waitclickP("set_working_directory_2.png",0.8,0)
        
        type(file_path + file_title + "/" + str(spec_num))
        wait(3)
        type(Key.ENTER)
        
       
    
        waitclickP("load_output_files.png",0.8,0)
    
        waitclickP("open_output_file.png",0.8,0)
        
        type(file_title + "_sup.out")
    
        
        type(Key.ENTER)
        
        wait2clickP("confirm_study_ids.png",0.79,0)
     
        wait(3)
        for i in range(9):
            type(Key.BACKSPACE)

        wait(3)
        
        paste(file_title + "_" + str(spec_num) + "_" + "1" + ".csv")
    
       
    
        wait2clickP("confirm_save_file_name.png",0.75,0)
        wait2clickP("calculate_amplitudes_and_crlbs.png",0.8,0)
    
    
        
        
#        # Brain Extraction
#
#        wait2clickP("brain_extraction.png",0.6,0)
#        wait2clickP("select_image_files.png",0.74,0)
#
#        wait(2)
#        type( file_title + ".nii.gz")
#        type(Key.ENTER)
#
#        wait2clickP("reorient_images.png",0.72,0)
#        waitclickP("launch_fslview.png",0.72,0)
#
#        waitclickP("cursor_tools.png",0.8,1)
#
#        wait(2)
#
#        wait2clickPTO("x.png",0.72,0,30,0)
#
#        type("c", KEY_CTRL)
#        wait(3)
#        x = Env.getClipboard()
#
#        wait2clickPTO("y.png",0.72,0,30,0)
#
#        type("c", KEY_CTRL)
#        wait(3)
#        y = Env.getClipboard()
#
#        wait2clickPTO("z.png",0.72,0,30,0)
#
#        type("c",KEY_CTRL)
#        wait(3)
#        z = Env.getClipboard()
#
#        closeNow()
#
#        wait2clickPTO("x-y-z.png",0.73,0,-360,1)
#
#        type(x)
#
#        wait2clickPTO("x-y-z.png",0.73,0,26,0)
#
#        type(y)
#
#        wait2clickPTO("x-y-z.png",0.73,0,360,0)
#
#        type(z)
#
#        wait2clickP("confirm_brain_isocenter.png",0.73,0)
#
#
#
#
#        type(Key.BACKSPACE)
#
#        type("0.2")
#
#
#        wait2clickP("confirm_test_thresholds.png",0.82,0)
#
#
#        wait2clickP("run_test_fsl.png",0.71,0)
#
#
#        wait2clickP("check_test_thresholds.png",0.73,0)
#
#        waitP("cursor_tools.png",0.8,1)
#
#        closeNow()
#
#        wait2clickP("confirm_intensity_threshold.png",0.73,0)
#
#
#
#
#        waitP("run_brain_extraction.png",0.71,1)
#
#        wait2clickP("run_brain_extraction.png",0.71,0)
#
#        waitP("run_brain_extraction_2.png",0.71,1)
#
#        wait2clickP("brain_segmentation.png",0.72,0)
#
#
#        wait2clickP("select_brain_extracted_image_files.png",0.71,1)
#
#        try:
#            wait2clickP("open_image_file.png",0.6,0)
#        except:
#            pass
#        type( file_title + "_std_brain.nii.gz")
#        type(Key.ENTER)
#
#        wait2clickP("confirm_image_type.png",0.71,0)
#
#        wait2clickP("confirm_fast_settings.png",0.71,0)
#
#        if spec_num == 0:
#            print("PVS TIME")
#            tic()
#
#            wait2clickP("run_pvs.png",0.74,0)
#
#            for i in range(2):
#                wait(180)
#                screen.click()
#
#
#            waitclickP("done.png",0.71,1)
#
#            toc()
#        else:
#            # this part is a little code that copies the Partial Volume Segmentation file for the first spectra to the current spec_num folder
#            wait(3)
#            terminal()
#            wait(3)
#            type("n",Key.CTRL + Key.SHIFT)
#            wait(3)
#            #Env.setClipboard("cp -R " + file_path + file_title + "/" + "1" + "/" + file_title + "_uns.out " +  file_path + file_title + "/" + str(spec_num) )
#            Env.setClipboard("cp -R " + file_path + file_title + "/" + "1" + "/" + file_title + "_uns.out " + file_path + file_title + "/" + "1" + "/" + file_title + "_std_brain_seg.nii.gz " + file_path + file_title + "/" + "1" + "/" + file_title + "_std_brain_pvseg.nii.gz " + file_path + file_title + "/" + str(spec_num) )
#            type("v",Key.CTRL + Key.SHIFT)
#            type(Key.ENTER)
#            wait(3)
#            closeNow()
#            waitclickP("minus.png",0.8,0)
        
            
    
    
        
        waitP("set_parameters.png",0.71,1)
        
    
    
    
        wait2clickP("set_parameters.png",0.71,0)
    
      
    
        wait2clickP("Load.png",0.71,0)
    
        wait(3)
        
        type("metab7T_te100_pjeon.qinfo")
    
        
        type(Key.ENTER)
        
    
       
      
    
        wait2clickP("confirm_quantification_parameters.png",0.71,0)
    
        
       
    
        wait2clickP("quantify_metabolites.png",0.71,0)
    
        
        
    
        wait2clickP("load_suppressed_out_files.png",0.71,0)
    
        
        wait(3)
        type(file_title + "_sup.out" + Key.ENTER)

        wait(3)
        for i in range(9):
            type(Key.BACKSPACE)
        wait(3)
        
        paste(file_title + "_" + str(spec_num) + "_" + "2" + ".csv")
    
    
       
        wait2clickP("confirm_save_file_name.png",0.75,0)
        
        wait(3)
        
    
        wait2clickP("run_quantification.png",0.71,0)
    
        #wait2clickP("run_quantification_done.png",0.71,0)
        wait(10)
        
        closeNow()
        wait(3)
        terminal()
        toc()
except: 
    print("oh no")
    if edit=="Y":
        voxel_de_adjust()


if ((flawed=="Y") and (inner_re_edit != "Y")):
    voxel_de_adjust()


# here is a little script that generates folders for the csv files. 

def csvFolder():
    wait(3)
    type("t",Key.CTRL + Key.ALT)
    wait(3)
    Env.setClipboard("cd Documents" + Key.ENTER)
    type("v",Key.CTRL + Key.SHIFT)
    wait(3)
    type("mkdir CSVFOLDER" + Key.ENTER)
    for i in range(1,(num_of_spec + 1)) :      
        Env.setClipboard("cp -R " + file_title + "/" + str(i) + "/" + file_title + "_" + str(i)   + "_1.csv "  + file_title + "/" + str(i) + "/" + file_title + "_" + str(i)   + "_2.csv " + "CSVFOLDER")
        type("v",Key.CTRL + Key.SHIFT)
        type(Key.ENTER)
    Env.setClipboard("cp -R " + "/media/sf_SpecFit/XLSX.py " + "CSVFOLDER" )
    type("v",Key.CTRL + Key.SHIFT)
    type(Key.ENTER)
csvFolder()

wait(3)
type("t",Key.CTRL + Key.ALT)
wait(3)
Env.setClipboard("cd Documents" + Key.ENTER)
type("v",Key.CTRL + Key.SHIFT)
wait(3)
type("cd CSVFOLDER" + Key.ENTER)
wait(3)
type("python XLSX.py" + Key.ENTER)
wait(1)
type("cd .." + Key.ENTER)
wait(1)
type("mv " file_title + " " file_title + "spec" + str(num_of_spec))
wait(1)
type(Key.ENTER)




toc() # returns "Elapsed time: 5.00 seconds."



