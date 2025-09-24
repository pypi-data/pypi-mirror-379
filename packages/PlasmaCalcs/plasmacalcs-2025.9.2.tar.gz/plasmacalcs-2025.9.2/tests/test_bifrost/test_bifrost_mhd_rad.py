"""
File Purpose: testing MhdRadiativeLoader functionality, using bifrost data as example.
"""
import os

import numpy as np
import pytest

import PlasmaCalcs as pc

HERE = os.path.dirname(__file__)


### --------------------- making bifrost calculator --------------------- ###

def get_bifrost_calculator(**kw_init):
    '''make a bifrost calculator'''
    with pc.InDir(os.path.join(HERE, 'test_bifrost_tinybox')):
        bc = pc.BifrostCalculator(**kw_init)
    return bc

def get_bifrost_multifluid_calculator(**kw_init):
    '''make a multifluid bifrost calculator (for multifluid analysis of bifrost outputs)'''
    with pc.InDir(os.path.join(HERE, 'test_bifrost_tinybox')):
        bm = pc.BifrostMultifluidCalculator(**kw_init)
    return bm


### --------------------- getting various vars --------------------- ###

def test_bifrost_emiss_vars():
    '''testing emiss-related vars and options, using Bifrost data'''
    bc = get_bifrost_calculator()
    bm = get_bifrost_multifluid_calculator()
    # emiss stuff (vdems need emiss)
    bc.tree('emiss')   # just checking it doesn't crash
    bm.tree('emiss')
    bc.emiss_mode = 'notrac_noopa'
    tree1 = bc.tree('emiss')
    assert tree1.contains_var('emiss_notrac')
    assert not tree1.contains_var('emiss_trac')
    assert not tree1.contains_var('tau')
    tree2 = bc.tree('emiss', emiss_mode='trac_opa')
    assert tree2.contains_var('emiss_trac')
    assert tree2.contains_var('tau')
    bc('emiss')  # just checking it doesn't crash
    with pytest.raises(pc.DimensionalityError):  # can't get emiss_trac for 2D box! needs 3D.
        bc('emiss', emiss_mode='trac_noopa')
    with pytest.raises(pc.FluidValueError):  # don't do emiss for multifluid!
        bm('emiss')
    bm('SF_emiss')  # multifluid calculator can specify single-fluid mode to get emiss.


def test_bifrost_vdem_vars():
    '''testing vdem-related vars and options, using Bifrost data'''
    bc = get_bifrost_calculator()
    # ensure can get vdems without crash.
    # (this is a tiny simulation box otherwise these would be wayyyy too expensive to do quickly):
    assert len(bc.VDEM_MODE_OPTIONS) >= 1  # i.e., the loop below is nontrivial...
    for x in ['x', 'z']:
        for vdem_mode in bc.VDEM_MODE_OPTIONS:
            bc(f'vdem_{x}', vdem_mode=vdem_mode)  # just checking it doesn't crash.
    # ensure vdem does crash if multiple components
    with pytest.raises(pc.ComponentValueError):
        bc('vdem', component=['x', 'z'])
    # check some dependencies
    bc.component = 'z'  # let's just stick with vdem_z for everything below.
    bc.tree('vdem')  # just checking it doesn't crash
    tree1 = bc.tree('vdem', vdem_mode='interp')
    assert tree1.contains_var('vdem_interp')
    assert not tree1.contains_var('vdem_no_interp')
    tree2 = bc.tree('vdem', vdem_mode='nointerp')
    assert tree2.contains_var('vdem_no_interp')
    tree3 = bc.tree('vdem', vdem_mode='allinterp')
    assert tree3.contains_var('vdem_allinterp')
    # vdem-related options
    assert np.all(bc('rcoords_logT') == bc.rcoords_logT)
    assert np.all(bc('rcoords_vdop', units='si') == bc.rcoords_vdop_kms * 1e3)
    # ensure can't set vdem options to invalid values:
    bc.rcoords_logT = np.arange(4.5, 6, 0.1)
    bc.vdem_logT_min = 4
    with pytest.raises(pc.InputError):
        bc.rcoords_logT = np.arange(3, 5, 0.1)  # can't set logT with minimum < vdem_logT_min
    with pytest.raises(pc.InputError):
        bc.vdem_logT_min = 5  # can't set vdem_logT_min > min(logT)
    # set appropriate options for the tinybox region selected here,
    #  then double-check that they were actually updated
    bc.set_attrs(component='z', vdem_mode='interp', vdem_logT_min=0,
                 rcoords_logT=np.arange(3, 5, 0.2),
                 rcoords_vdop_kms=np.arange(-20, 20, 5))
    assert np.all(bc('rcoords_logT') == np.arange(3, 5, 0.2))
    assert np.all(bc('rcoords_vdop', units='si') == bc.rcoords_vdop_kms * 1e3)
    # compute vdem and double-check some things
    vdem0 = bc('vdem')
    assert np.all(vdem0.sel(logT=slice(None, 3.3)) == 0)  # nothing in tinybox at "very cold" temps
    assert np.all(vdem0.sel(logT=slice(4.3, None)) == 0)  # nothing in tinybox at "very hot" temps
    assert not np.all(vdem0.sel(logT=slice(3.3, 4.3)) == 0)  # something nonzero in the middle.
    assert np.all(vdem0.sel(vdop=slice(None, -12)) == 0)  # nothing in tinybox at "very fast" -u
    assert np.all(vdem0.sel(vdop=slice(12, None)) == 0)  # nothing in tinybox at "very fast" +u
    assert not np.all(vdem0.sel(vdop=slice(-12, 12)) == 0)  # something nonzero in the middle.
    # hard-coded: computed some values on 2025-09-22. Hopefully they don't change.
    # (if they do change, test will fail. Then can choose if test should be updated, or if it was a bug.)
    # (giving a little bit of buffer room in case of different floating point rounding schemes.)
    assert 2.25e8 < vdem0.max() < 2.35e8
    assert 1.25e3 < vdem0.where(vdem0 > 0).min() < 1.35e3
    assert 1.40e6 < vdem0.mean() < 1.50e6
    assert 2.15e6 < vdem0.where(vdem0 > 0).median() < 2.25e6
    assert vdem0.where(vdem0 > 0).count() == 325  # number of nonzero points in vdem


def test_bifrost_Gofnt_vars():
    '''testing G(T)-related vars and options, using Bifrost data'''
    bc = get_bifrost_calculator()
    bc.tree('GofT_fe_9_ion')  # just checking it doesn't crash
    tree = bc.tree('spectra_fe_9_ion_prof')
    assert tree.contains_var('GofT_fe_9_ion_em')
    # [TODO] more tests with GofT.
    # maybe including a test which actually computes values?
    #  The problem is, it depends on muse & chiantipy, which are not PlasmaCalcs dependencies.
    #  So, might not be able to do it in PlasmaCalcs autotests.
