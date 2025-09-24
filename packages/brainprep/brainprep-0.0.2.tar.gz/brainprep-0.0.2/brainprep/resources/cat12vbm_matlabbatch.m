%-----------------------------------------------------------------------
% Job saved on 26-Mar-2021 15:27:40 by cfg_util (rev $Rev: 7345 $)
% spm SPM - Unknown
% cfg_basicio BasicIO - Unknown
%-----------------------------------------------------------------------
%% https://www.linuxquestions.org/questions/slackware-14/libreoffice-libfontconfig-so-1-undefined-symbol-ft_done_mm_var-4175665794/

disp('brainprep CAT12 VBM')
if isempty(which('spm')),
     throw(MException('SPMCheck:NotFound', 'SPM not in matlab path'));
end
[name, version] = spm('ver');
fprintf('SPM version: %s Release: %s\n',name, version);
fprintf('SPM path: %s\n', which('spm'));

matlabbatch{{1}}.spm.tools.cat.estwrite.data = {{
    {anat_file}
}};
%%
matlabbatch{{1}}.spm.tools.cat.estwrite.data_wmh = {{''}};
matlabbatch{{1}}.spm.tools.cat.estwrite.nproc = 0;
matlabbatch{{1}}.spm.tools.cat.estwrite.useprior = '';
matlabbatch{{1}}.spm.tools.cat.estwrite.opts.tpm = {{'{tpm_file}'}};
matlabbatch{{1}}.spm.tools.cat.estwrite.opts.affreg = 'mni';
matlabbatch{{1}}.spm.tools.cat.estwrite.opts.biasstr = 0.5;
matlabbatch{{1}}.spm.tools.cat.estwrite.opts.accstr = 0.5;
matlabbatch{{1}}.spm.tools.cat.estwrite.extopts.segmentation.APP = 1070;
matlabbatch{{1}}.spm.tools.cat.estwrite.extopts.segmentation.NCstr = -Inf;
matlabbatch{{1}}.spm.tools.cat.estwrite.extopts.segmentation.spm_kamap = 0;
matlabbatch{{1}}.spm.tools.cat.estwrite.extopts.segmentation.LASstr = 0.5;
matlabbatch{{1}}.spm.tools.cat.estwrite.extopts.segmentation.gcutstr = 2;
matlabbatch{{1}}.spm.tools.cat.estwrite.extopts.segmentation.cleanupstr = 0.5;
matlabbatch{{1}}.spm.tools.cat.estwrite.extopts.segmentation.BVCstr = 0.5;
matlabbatch{{1}}.spm.tools.cat.estwrite.extopts.segmentation.WMHC = 1;
matlabbatch{{1}}.spm.tools.cat.estwrite.extopts.segmentation.SLC = 0;
matlabbatch{{1}}.spm.tools.cat.estwrite.extopts.segmentation.mrf = 1;
matlabbatch{{1}}.spm.tools.cat.estwrite.extopts.segmentation.restypes.optimal = [1 0.1];
matlabbatch{{1}}.spm.tools.cat.estwrite.extopts.registration.dartel.darteltpm = {{'{darteltpm_file}'}};
matlabbatch{{1}}.spm.tools.cat.estwrite.extopts.vox = 1.5;
matlabbatch{{1}}.spm.tools.cat.estwrite.extopts.surface.pbtres = 0.5;
matlabbatch{{1}}.spm.tools.cat.estwrite.extopts.surface.pbtmethod = 'pbt2x';
matlabbatch{{1}}.spm.tools.cat.estwrite.extopts.surface.pbtlas = 0;
matlabbatch{{1}}.spm.tools.cat.estwrite.extopts.surface.collcorr = 0;
matlabbatch{{1}}.spm.tools.cat.estwrite.extopts.surface.reduce_mesh = 1;
matlabbatch{{1}}.spm.tools.cat.estwrite.extopts.surface.vdist = 1.33333333333333;
matlabbatch{{1}}.spm.tools.cat.estwrite.extopts.surface.scale_cortex = 0.7;
matlabbatch{{1}}.spm.tools.cat.estwrite.extopts.surface.add_parahipp = 0.1;
matlabbatch{{1}}.spm.tools.cat.estwrite.extopts.surface.close_parahipp = 0;
matlabbatch{{1}}.spm.tools.cat.estwrite.extopts.admin.experimental = 0;
matlabbatch{{1}}.spm.tools.cat.estwrite.extopts.admin.new_release = 0;
matlabbatch{{1}}.spm.tools.cat.estwrite.extopts.admin.lazy = 0;
matlabbatch{{1}}.spm.tools.cat.estwrite.extopts.admin.ignoreErrors = 1;
matlabbatch{{1}}.spm.tools.cat.estwrite.extopts.admin.verb = 2;
matlabbatch{{1}}.spm.tools.cat.estwrite.extopts.admin.print = 2;
matlabbatch{{1}}.spm.tools.cat.estwrite.output.surface = 0;
matlabbatch{{1}}.spm.tools.cat.estwrite.output.surf_measures = 1;
matlabbatch{{1}}.spm.tools.cat.estwrite.output.ROImenu.atlases.neuromorphometrics = 1;
matlabbatch{{1}}.spm.tools.cat.estwrite.output.ROImenu.atlases.lpba40 = 0;
matlabbatch{{1}}.spm.tools.cat.estwrite.output.ROImenu.atlases.cobra = 0;
matlabbatch{{1}}.spm.tools.cat.estwrite.output.ROImenu.atlases.hammers = 0;
matlabbatch{{1}}.spm.tools.cat.estwrite.output.ROImenu.atlases.ibsr = 0;
matlabbatch{{1}}.spm.tools.cat.estwrite.output.ROImenu.atlases.aal3 = 0;
matlabbatch{{1}}.spm.tools.cat.estwrite.output.ROImenu.atlases.mori = 0;
matlabbatch{{1}}.spm.tools.cat.estwrite.output.ROImenu.atlases.anatomy = 0;
matlabbatch{{1}}.spm.tools.cat.estwrite.output.ROImenu.atlases.julichbrain = 0;
matlabbatch{{1}}.spm.tools.cat.estwrite.output.ROImenu.atlases.Schaefer2018_100Parcels_17Networks_order = 0;
matlabbatch{{1}}.spm.tools.cat.estwrite.output.ROImenu.atlases.Schaefer2018_200Parcels_17Networks_order = 0;
matlabbatch{{1}}.spm.tools.cat.estwrite.output.ROImenu.atlases.Schaefer2018_400Parcels_17Networks_order = 0;
matlabbatch{{1}}.spm.tools.cat.estwrite.output.ROImenu.atlases.Schaefer2018_600Parcels_17Networks_order = 0;
matlabbatch{{1}}.spm.tools.cat.estwrite.output.ROImenu.atlases.ownatlas = {{''}};
matlabbatch{{1}}.spm.tools.cat.estwrite.output.GM.native = 1;
matlabbatch{{1}}.spm.tools.cat.estwrite.output.GM.warped = 0;
matlabbatch{{1}}.spm.tools.cat.estwrite.output.GM.mod = 1;
matlabbatch{{1}}.spm.tools.cat.estwrite.output.GM.dartel = 0;
matlabbatch{{1}}.spm.tools.cat.estwrite.output.WM.native = 1;
matlabbatch{{1}}.spm.tools.cat.estwrite.output.WM.warped = 0;
matlabbatch{{1}}.spm.tools.cat.estwrite.output.WM.mod = 1;
matlabbatch{{1}}.spm.tools.cat.estwrite.output.WM.dartel = 0;
matlabbatch{{1}}.spm.tools.cat.estwrite.output.CSF.native = 1;
matlabbatch{{1}}.spm.tools.cat.estwrite.output.CSF.warped = 0;
matlabbatch{{1}}.spm.tools.cat.estwrite.output.CSF.mod = 1;
matlabbatch{{1}}.spm.tools.cat.estwrite.output.CSF.dartel = 0;
matlabbatch{{1}}.spm.tools.cat.estwrite.output.ct.native = 0;
matlabbatch{{1}}.spm.tools.cat.estwrite.output.ct.warped = 0;
matlabbatch{{1}}.spm.tools.cat.estwrite.output.ct.dartel = 0;
matlabbatch{{1}}.spm.tools.cat.estwrite.output.pp.native = 0;
matlabbatch{{1}}.spm.tools.cat.estwrite.output.pp.warped = 0;
matlabbatch{{1}}.spm.tools.cat.estwrite.output.pp.dartel = 0;
matlabbatch{{1}}.spm.tools.cat.estwrite.output.WMH.native = 0;
matlabbatch{{1}}.spm.tools.cat.estwrite.output.WMH.warped = 0;
matlabbatch{{1}}.spm.tools.cat.estwrite.output.WMH.mod = 0;
matlabbatch{{1}}.spm.tools.cat.estwrite.output.WMH.dartel = 0;
matlabbatch{{1}}.spm.tools.cat.estwrite.output.SL.native = 0;
matlabbatch{{1}}.spm.tools.cat.estwrite.output.SL.warped = 0;
matlabbatch{{1}}.spm.tools.cat.estwrite.output.SL.mod = 0;
matlabbatch{{1}}.spm.tools.cat.estwrite.output.SL.dartel = 0;
matlabbatch{{1}}.spm.tools.cat.estwrite.output.TPMC.native = 0;
matlabbatch{{1}}.spm.tools.cat.estwrite.output.TPMC.warped = 0;
matlabbatch{{1}}.spm.tools.cat.estwrite.output.TPMC.mod = 0;
matlabbatch{{1}}.spm.tools.cat.estwrite.output.TPMC.dartel = 0;
matlabbatch{{1}}.spm.tools.cat.estwrite.output.atlas.native = 0;
matlabbatch{{1}}.spm.tools.cat.estwrite.output.atlas.warped = 0;
matlabbatch{{1}}.spm.tools.cat.estwrite.output.atlas.dartel = 0;
matlabbatch{{1}}.spm.tools.cat.estwrite.output.label.native = 0;
matlabbatch{{1}}.spm.tools.cat.estwrite.output.label.warped = 0;
matlabbatch{{1}}.spm.tools.cat.estwrite.output.label.dartel = 0;
matlabbatch{{1}}.spm.tools.cat.estwrite.output.labelnative = 1;
matlabbatch{{1}}.spm.tools.cat.estwrite.output.bias.native = 0;
matlabbatch{{1}}.spm.tools.cat.estwrite.output.bias.warped = 1;
matlabbatch{{1}}.spm.tools.cat.estwrite.output.bias.dartel = 0;
matlabbatch{{1}}.spm.tools.cat.estwrite.output.las.native = 0;
matlabbatch{{1}}.spm.tools.cat.estwrite.output.las.warped = 0;
matlabbatch{{1}}.spm.tools.cat.estwrite.output.las.dartel = 0;
matlabbatch{{1}}.spm.tools.cat.estwrite.output.jacobianwarped = 0;
matlabbatch{{1}}.spm.tools.cat.estwrite.output.warps = [1 1];
matlabbatch{{1}}.spm.tools.cat.estwrite.output.rmat = 0;
