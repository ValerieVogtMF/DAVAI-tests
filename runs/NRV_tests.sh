#!/usr/bin/bash

davai_mkjob_run='python vortex/bin/mkjob.py -j profile=rd-belenos-mt'

# Arpege 4D Bator+Screening+Minim
#$davai_mkjob_run task=assim.BSM4D_arpege name=BSM4D_arpege

# Arome 3D Bator+Screening+Minim
$davai_mkjob_run task=assim.BSM3D_arome name=BSM3D_arome

#davai_mkjob_run task=forecasts.series name=fc-canonical-series
#davai_mkjob_run task=fullpos.series name=fullpos-canonical-series

echo "DAVAI NRV test bench launched through job scheduler !"
echo "Checkout Ciboulai for results !"