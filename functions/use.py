# -*- coding: utf-8 -*-
# Copyright (C) 2012, Almar Klein
#
# Visvis is distributed under the terms of the (new) BSD License.
# The full license can be found in 'license.txt'.
import visvis as vv

def use(backendName=None):
    """ use(backendName=None)
    
    Use the specified backend and return an App instance that has a Run()
    method to enter the GUI toolkit's mainloop, and a ProcessEvents()
    method to process any GUI events.
    
    This function is only required to explicitly choose a specific backend, 
    or to obtain the application object; when this function is not used,
    vv.figure() will select a backend automatically.
    
    Backend selection
    -----------------
    If no backend is given, returns the previously selected backend. If no
    backend was yet selected, a suitable backend is selected automatically.
    This is done by detecting whether any of the backend toolkits is
    already loaded. If not, visvis tries to load the 
    vv.settings.preferredBackend first.
    
    Note: the backend can be changed even when figures are created with
    another backend, but this is not recommended.
    
    Example embedding in Qt4
    ------------------------
    # Near the end of the script:
    
    # Get app instance and create native app
    app = vv.use('qt4')
    app.Create() 
    
    # Create window
    m = MainWindow()
    m.resize(560, 420)
    m.show()
    
    # Run main loop
    app.Run()
    
    """
    return vv.backends.use(backendName)
