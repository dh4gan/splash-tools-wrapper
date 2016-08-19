# Written 18/8/16 by Duncan Forgan
# Stores data for using SPLASH as a file conversion tool
 
filetypes = ['gadget' ,'vine', 'sphNG', 'phantom', 'ndspmhd' ,'srosph' ,'dragon', 'seren', 'tipsy']
ntypes = len(filetypes)

splashexecutables = ['gsplash', 'vsplash', 'ssplash','ssplash', 'nsplash', 'rsplash', 'dsplash','srsplash', 'tsplash']

exec_dict = dict(zip(filetypes,splashexecutables))

