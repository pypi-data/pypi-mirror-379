![License](https://img.shields.io/pypi/l/iguape?style=plastic&color=green&link=https%3A%2F%2Fpypi.org%2Fproject%2Figuape%2F)
![Version](https://img.shields.io/pypi/v/iguape?style=plastic&color=pink)
![Status](https://img.shields.io/pypi/status/iguape?style=plastic&link=https%3A%2F%2Fpypi.org%2Fproject%2Figuape%2F
)
# Iguape - Paineira Graphical User Interface


## Description
Iguape is a graphical user interface designed to help users during *in situ* experiments at Paineira. Via Iguape the user can visualize the numerous XRD patterns generated throughout the experiments. The program allows for peak fitting at a selected angle interval.  

## Visuals
The GUI has two tabs and concentrate its features in a button panel at the bottom of the window. The XRD Data tab displays the diffraction patterns stacked by a user-defined offset. The Peak Fitting tab displays the data obtained through peak fitting of the XRD patterns on the selected 2theta interval.
![Iguape_XRD_Data_Main_Window](https://github.com/user-attachments/assets/fffae287-6076-495d-a3fe-dc6e4289b7c0)
![Iguape_Peak_Fit_PsdVoigt](https://github.com/user-attachments/assets/4c7c9224-88ac-41ad-bcb7-c248986fdfb3)
## Installation
When using Linux, you can download Iguape via pip, with the console command:
```bash
pip install iguape
iguape #this will open the software, once it's installed
```
For Windows, a instaler can be found in the following link: [Windows Installer]()
## Usage
# **Initialization**
The first step, once Iguape is initialized, is to select a folder to monitor. This can be done by clicking in the **Folder** option at the upper right corner of the window. It's important that the selected folder contains the iguape_fileslist.txt file. It is though this text document, that Iguape can read the XRD data available at the Folder. 
![Initialization](https://github.com/user-attachments/assets/01f48445-52b8-4c89-afb8-43136d05c2d8)
# **Custom Vizualization**
Iguape offers tools for custom visualization of the XRD patterns. These include: XRD patterns offset, 2theta and temperature/measure order masks, zoom, pan and figure saving.
![Iguape_tools](https://github.com/user-attachments/assets/785404f5-761b-444a-9f41-3b601b62aaa8)
![Iguape_tools#2](https://github.com/user-attachments/assets/5d5267a4-516c-45af-b2d4-3173848b98b0)

# **Peak Fit**
Peak fitting is available in Iguape, helping the analysis of sample evotution during _in situ_ experiments. When the Peak Fit button is pressed, a new window will be opened. The user, then, can configure the fitting model and have a preview of the best fit achieved by Iguape.  
![PeakFIt](https://github.com/user-attachments/assets/3bedf4d9-e06d-4b84-a5a0-9cecd292adbd)
![Iguape_Peak_Fit_Window_2xPsdVoigt](https://github.com/user-attachments/assets/38ef0b40-ea7d-436d-a140-c3b40f8ac19b)
## Support
Any enquiries can be adressed to joao.neto@lnls.br. Please, fell free to suggest or correct anything.

## Authors and acknowledgment
João Luis Biondo Neto;
Junior Cintra Mauricio

## License
This project is under the GNU-GPL 3.0. For more information, see LICENSE.txt

## Citation
Biondo Neto, J. L., Cintra Mauricio, J. & Rodella, C. B. (2025). J. Appl. Cryst. 58, 1061-1067. **DOI**: https://doi.org/10.1107/S1600576725003309
```bibtext
    @article{BiondoNeto:yr5153,
        author = "Biondo Neto, Jo{\~{a}}o L. and Cintra Mauricio, Junior and Rodella, Cristiane B.",
        title = "{{\it IGUAPE}, a graphical user interface for {\it in situ/operando} X-ray diffraction experiments at the PAINEIRA beamline: development and application}",
        journal = "Journal of Applied Crystallography",
        year = "2025",
        volume = "58",
        number = "3",
        pages = "1061--1067",
        month = "Jun",
        doi = {10.1107/S1600576725003309},
        url = {https://doi.org/10.1107/S1600576725003309},
        abstract = {Synchrotron radiation X-ray diffraction facilities equipped with fast area detectors can generate X-ray diffraction (XRD) patterns in seconds. This capability is fundamental to revealing transient crystalline phases and the structural evolution of samples and devices for technology applications. However, it generates XRD patterns usually faster than the user can process during the experiment. Thus, an open-source and user-friendly software package named {\it IGUAPE} was developed for the PAINEIRA beamline (Sirius, Brazil). It allows visualization of the X-ray diffractograms as soon as the azimuthal integration of the Debye rings is processed and the XRD pattern is created. The software can also perform a single-peak qualitative analysis of the diffraction data. Upon selecting a diffraction peak in the XRD pattern, the peak position, integrated area and full width at half-maximum variation during the {\it in situ} or {\it operando} experiment are given.},
        keywords = {open-source software, <it>IGUAPE</it>, X-ray diffraction, XRD, PAINEIRA beamline, <it>in situ</it> experiments},
    }
```


## Project status
Iguape is fully operational at Paineira. Working on distribution for Paineira users.
