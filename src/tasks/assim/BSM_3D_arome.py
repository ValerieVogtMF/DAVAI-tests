# -*- coding: utf-8 -*-

from __future__ import print_function, absolute_import, unicode_literals, division

import vortex
from vortex import toolbox
from vortex.layout.nodes import Driver, Family, LoopFamily

from .raw2odb.batodbLAM import BatorODB
#from .screenings.screeningCNT0_LAM3D import Screening as ScreeningCNT0
#from .minims.minimCNT0_LAM3D import Minim as MinimCNT0
from .screenings.screeningOOPS_LAM3D import ScreeningOOPS
from .minims.minimOOPS_LAM3D import MinimNoVARBC as MinimOOPSNoVARBC
from .minims.AnalyseOOPS_LAM3D import AnalyseLAM3D as AnalysisOOPS


def setup(t, **kw):
    return Driver(tag='drv', ticket=t, options=kw, nodes=[
        Family(tag='arome', ticket=t, nodes=[
            Family(tag='3dvar3h', ticket=t, nodes=[
                Family(tag='default_compilation_flavour', ticket=t, nodes=[
                    LoopFamily(tag='rundates', ticket=t,
                        loopconf='rundates',
                        loopsuffix='.{}',
                        nodes=[
                        Family('BSM', ticket=t, on_error='delayed_fail', nodes=[
                            BatorODB(tag='batodb', ticket=t, **kw),
                                # delayed_fail to let the minimOOPS run before raising error
                            #Family('cnt0', ticket=t, on_error='delayed_fail', nodes=[
                                #ScreeningCNT0(tag='screeningCNT0', ticket=t, **kw),
                                #MinimCNT0(tag='minimCNT0', ticket=t, **kw)
                            #    ], **kw),
                            Family('oops', ticket=t, nodes=[
                                ScreeningOOPS(tag='screeningOOPS', ticket=t, **kw),
                                MinimOOPSNoVARBC(tag='minimOOPS-novarbc', ticket=t, **kw)
                                ], **kw),
                            AnalysisOOPS(tag='analysis', ticket=t, **kw)
                            ], **kw),
                        ], **kw),
                    ], **kw),
                ], **kw),
            ], **kw),
        ],
    )

