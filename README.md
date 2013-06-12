bild
====
**********************************************************
BILDER README FILE
(C) 2013 Omar Metwally 

How to use bilder:

1. Set up a MySQL database and update the 'settings.py' file with the corresponding database name, username, and password.

2. Train the software:
  a. Put jpeg files in the folder 'sourceimages'
	b. Put DICOM files in the folder 'xsourceimages'
	c. Start the Django development server (or run your production server)	
	b. Go to 'localhost:8000/remember' (or 'localhost:8000/xremember') to compress the images and store them in your MySQL database

3. The input image(s) should be put in the folder 'inputimage' (if JPEG) or 'xinputimage' (if DICOM). This folder MUST BE EMPTY except for a single image until the bug preventing multiple input images is resolved.

4. Go to 'localhost:8000/detect/' (if using input JPEGS) or 'localhost:8000/xdetect/' (if using input DICOM). A marked image named 'input.marked'
will be created the 'markedimage' folder.



   *   *   *   *   *
Legal notices:
Bilder is not a tool for diagnosis or replacement for medical evaluation by a healthcare professional. It is a research tool that must not be used for any patient-care purposes. You assume all responsibility for use and potential liability associated with any use of this software. Bilder is not FDA-approved and is not designed to be HIPAA-compatible. By using this software you agree to abide by all regional and federal laws and all laws pertaining to protection of patient information. Under no circumstances may this software be used with identifying patient information.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS ``AS IS'' AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE AUTHORS OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

     *   *   *   *   *
This software utilizes the Python Imaging Library (PIL) and pydicom.

PIL Copyright 1997-2011 by Secret Labs AB
PIL Copyright 1995-2011 by Fredrik Lundh

"Secret Labs AB and the author disclaims all warranties
with regard to this software, including all implied 
warranies of merchantability and fitness. In no event
shall Secret Labs AB or the author be liable for any
special, indirect or consequential damages or any damages
whatsoever resulting from loss of use, data or profits,
whether in an action of contract, negligence or other 
tortious action, arising out of or in connection with the
use or performance of this software."


pydicom Copyright (c) 2008-2010 Darcy Mason and pydicom contributors

"Except for portions outlined below, pydicom is released under an MIT license:

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

Portions of pydicom (private dictionary file(s)) were generated from the
private dictionary of the GDCM library, released under the following license:

Program: GDCM (Grassroots DICOM). A DICOM library
Module: http://gdcm.sourceforge.net/Copyright.html

Copyright (c) 2006-2010 Mathieu Malaterre
Copyright (c) 1993-2005 CREATIS
(CREATIS = Centre de Recherche et d'Applications en Traitement de l'Image)
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

* Redistributions of source code must retain the above copyright notice,
this list of conditions and the following disclaimer.

* Redistributions in binary form must reproduce the above copyright notice,
this list of conditions and the following disclaimer in the documentation
and/or other materials provided with the distribution.

* Neither name of Mathieu Malaterre, or CREATIS, nor the names of any
contributors (CNRS, INSERM, UCB, Universite Lyon I), may be used to
endorse or promote products derived from this software without specific
prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS ``AS IS'' AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE AUTHORS OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
**********************************************************


