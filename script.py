import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from plotnine import *
import warnings
warnings.filterwarnings("ignore")
data=pd.read_csv(sys.argv[1])
data_es=data.where(data['Region']=='es').where(data['Position']<=2).dropna()
gg=ggplot(data_es)+aes(x='Track Name', y='Streams', color='Artist')+geom_point(size=2)+ ggtitle('Canciones más escuchadas en España en 2017')+ theme(axis_text_x  = element_text(angle = 90, hjust = 1))
print(gg)
ggsave(gg,'plot.jpg')