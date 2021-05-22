# Variables

```
R_SpriteSector                 = 1                                   ### Use sector visibility for sprites
NodeFXSpringDebug              = 0                                   ### NodeFX Spring override (0/1)
NodeFXSpringShow               = 0                                   ### NodeFX Spring debug info
NodeFXSpringMSec               = 50                                  ### NodeFX Spring calc. period (msec)
NodeFXSpringMidP               = 0.500000                            ### NodeFX Spring mid-point
NodeFXSpringRotX               = 0.000000                            ### NodeFX Spring rotation x (deg)
NodeFXSpringRot                = 0.500000                            ### NodeFX Spring rotation coef.
NodeFXSpringCoef2              = 0.600000                            ### NodeFX Spring coef. 2
NodeFXSpringCoef1              = 0.600000                            ### NodeFX Spring coef. 1
NodeFXWheelShow                = 0                                   ### NodeFX Wheel debug info
NodeFXWheelSlide               = 1.000000                            ### NodeFX Wheel sliding factor
NodeFXWheelRadius              = 1.000000                            ### NodeFX Wheel radius multiplier
R_AnimNodo_Count               = 5734                                ### AnimNodo counter
OptAnimPosMax                  = 2000.000000                         ### AnimPos compression max dist
OptAnimFovErr                  = 0.010000                            ### AnimFOV optimization epsilon (deg)
OptAnimRotErr                  = 0.030000                            ### AnimRot optimization epsilon (deg)
OptAnimPosErr                  = 0.010000                            ### AnimPos optimization epsilon
OptimizeAnims                  = 1                                   ### 0=none, 1=Compact anims
R_UsePortals                   = 1                                   ### Use portals (0/1)
R_ShowPortals                  = 0                                   ### Show portals (0/1/2/3)
FastGetYSector                 = 1                                   ### Fast GetYSector (0/1)
R_ShowPreIllumVtx              = 0                                   ### Show preilluminated vertex objects (0|1|2)
SharedTexuresPath              = 2D/Textures/Shared/                 ### Default path for shared textures ($name.bmp)
SM3_CheckTime                  = 1                                   ### Check filetime of SM3 files (0/1)
SM3_UseScenes                  = 1                                   ### Read/Write SM3 files (0/1/2)
CM3_DeleteM3D                  = 0                                   ### Delete M3D file after CM3 creation (0/1)
CM3_CheckTime                  = 1                                   ### Check filetime of CM3 files (0/1)
CM3_UseScenes                  = 1                                   ### Read/Write CM3 files (0/1/2)
ShowNodesTree                  = 0                                   ### Show nodes tree at model M3D loading time (0/1)
OptimizeNodes                  = 7                                   ### 0=none, 1=delete unused nodes, 2=colapse to bip nodes, 4=AniMask, 7=all
UseWSM                         = 0                                   ### Use ObjTMAfterWSM (0/1)
R_MeshCache                    = 1                                   ### Use mesh cache for non-transparent nodes (0/1, 10=info)
R_TranspZBias                  = 200.000000                          ### Transp. sort z-bias (def. 200.0)
R_ShowTranspBox                = 0                                   ### Show transparent nodes (0/1)
R_ParticlesZBias               = 1                                   ### Particle ZBias (0/1)
R_ParticlesAlphaDist           = 1                                   ### Particle Alpha Dist Attenuation
R_ParticlesLock                = 0                                   ### Particle Lock mode (1=always discard)
R_ParticlesDraw                = 1                                   ### Render Particle Primitives
R_ParticlesOne                 = 0                                   ### Render only first particle on the Vertex Buffer
R_MaxSparkSize                 = 20.000000                           ### Max spark size
R_MinSparkDist                 = 1.000000                            ### Min spark distance to camera
R_ShowEVA                      = 0                                   ### Show vertex anim. (0/1)
R_UseEVA                       = 1                                   ### Use vertex anim. (0/1)
R_ShowSkin                     = 0                                   ### Show skinning (0/1)
R_UseSkin                      = 1                                   ### Use skinning (0/1)
R_SkipModelFX                  = 0                                   ### Disable model effects (0/1)
R_VideoLockShow                = 0                                   ### Video frame lock show quad
R_VideoLockBuf                 = 1                                   ### Video frame lock buffers (1/2/3)
R_VideoLockMode                = 1                                   ### Video frame lock mode (0/1/2/3)
VideoScaleBlue                 = 1.000000                            ### Video blue color scale (def. 1.0)
VideoScaleGreen                = 1.000000                            ### Video green color scale (def. 1.0)
VideoScaleRed                  = 1.000000                            ### Video red color scale (def. 1.0)
VideoScaleRGB                  = 1.000000                            ### Video color scale (def. 1.0)
VideoGammaRGB                  = 1.000000                            ### Video color gamma (def. 1.0)
R_LensFlare                    = 1                                   ### Render LensFlare (0/1)
R_Trails                       = 1                                   ### Render Trails (0/1)
R_NodoR_Count                  = 5860                                ### NodoR counter
MonitorAmbient                 = 0                                   ### Ambient light for EnableMonitorLights (def. 0)
R_LightMult2                   = 1.000000                            ### Vertex lighting multiplier in atten2 mode (def. 1.0)
R_LightAtten2                  = 0                                   ### Use alternate attenuation mode (0/1)
R_LightSector                  = 1                                   ### Use light sector (0/1)
R_LightEnaD3D                  = 1                                   ### Use light enable cache (0/1)
R_LightTrace                   = 0                                   ### Use model to light raytracing (0/1)
R_LightDefer                   = 1                                   ### Use deferred light activation (0/1)
R_LightTarget                  = 1                                   ### Use target nodes (0/1)
R_SpotlightAng                 = 1                                   ### Discard spotlights by falloff angle (0/1)
R_LightSortI                   = 1.000000                            ### Light sorting intensity weight (def. 1.0)
R_LightSort                    = 12                                  ### Max. sorted lights (0..16)
R_LightAmbient                 = 0.000000                            ### Vertex lighting ambient amount (def. 0.0)
R_LightDesat                   = 0.000000                            ### Vertex lighting desaturation (def. 0.0)
R_LightGamma                   = 1.000000                            ### Vertex lighting gamma (def. 1.0)
R_LightMult                    = 1.000000                            ### Vertex lighting multiplier (def. 1.0)
R_LightAtten                   = 5.000000                            ### Vertex lighting atten. factor (def. 5.0)
R_ShowLights                   = 0                                   ### Show lights (0/1)
R_PortalBand                   = 0                                   ### Portal clipping viewport margin
R_PortalClip                   = 1                                   ### Use portal viewport for clipping (0/1)
R_PortalEnd                    = 1                                   ### Use end sectors (0/1)
R_PortalExt                    = 1                                   ### Use sector visibility extension (0/1/2)
R_PortalPos                    = 1                                   ### Use sector position cache (0/1)
R_PortalNorm                   = 1                                   ### Use portal plane normal (0/1)
R_PortalDist                   = 20.000000                           ### Portal min. distance factor
BuildMST                       = 1                                   ### Build and load MultiSprite MST files (0/1)
MovieFramerate                 = 30                                  ### Movie FPS for avi recording
MovieJpegQuality               = 95                                  ### JPEG quality for movies (0..100)
MovieCacheSize                 = 256                                 ### File buffer size for movies (Megabytes)
MovieUseMemory                 = 0                                   ### Movie uses RAM instead of HD (0/1)
R_Nodo3D_Count                 = 2505                                ### Node3D counter
R_NodeSlerp2                   = 1                                   ### Slerp2 mode for nodes (0/1/2)
R_SkipNodeFX                   = 0                                   ### Disable node effects (0/1)
R_SkipAnimVis                  = 0                                   ### Disable node visibility anim (0/1)
R_SkipAnim                     = 0                                   ### Disable node animation (0/1)
R_SkipTrans2                   = 1                                   ### Disable stencil node transform (0/1)
R_SkipTrans                    = 0                                   ### Disable node transform (0/1)
R_SkipNodes                    = 0                                   ### Disable node rendering (0/1)
R_ShowLBoxName                 =                                     ### Show nodes hierarchy and bbox (filter)
R_ShowLBoxMax                  = 0                                   ### Show nodes hierarchy and bbox (max. node)
R_ShowLBoxMin                  = 0                                   ### Show nodes hierarchy and bbox (min. node)
R_ShowLocalBox                 = 0                                   ### Show nodes hierarchy and bbox (0/1)

PlayVideoFX                    = 0                                   ### Video playback image fx (1=MirrorY,2=MirrorX)
R_ShowFlaresInfo               = 0                                   ### Show flares debug info (0/1)
R_SkipFlares                   = 1                                   ### Disable flares rendering (0/1)
R_SortInvert                   = 0                                   ### Invert models sorting (0/1)
R_SortShow                     = 0                                   ### Show sorting info (0/1/2)
R_SortModels                   = 1                                   ### Sort models by distance
R_DistMStencil                 = 2500.000000                         ### Model Stencil distance when not visible
R_DistMLOD1                    = 1.000000                            ### Model LOD 1 distance coef.
R_DrawMLODMin                  = 0                                   ### Set most detailed LOD to draw (1..n)
R_DrawMLODPart                 = 1                                   ### Draw model LOD particles (0/1)
R_DrawMLODMask                 = 0                                   ### Draw model LOD Mask
R_UseMLOD                      = 1                                   ### Use model LODs
R_LightLimit                   = 4                                   ### Max. enabled lights per model (0..6)
R_AnimInterpMult               = 1.000000                            ### Multiplier of interpolation between animations
R_SkipAnimInterp               = 0                                   ### Disable interpolation between animations (0/1)
R_SkipUpdateVis                = 0                                   ### Skip model visibility test (0/1)
R_ModelFastIsVis               = 1                                   ### Use FastIsVisible for model visibility pre-test (0/1/2)
R_ModelPortalVis               = 1                                   ### Use portals for model visibility test (0/1)
R_ShowModelSector              = 0                                   ### Show model sector (0/1/2)
R_ShowModelLights              = 0                                   ### Show model lights (0/1/2)
R_ShowModelPos                 = 0                                   ### Show model position (0/1/2)
R_ShowModelBox                 = 0                                   ### Show model bounding box (0/1/2/3)

AnalizeQuads                   = 0                                   ### Analize problems in quads.
ShowMapQDist                   = 0.000000                            ### Show map collision quads distance
ShowMapQuads                   = 0                                   ### Show map collision quads (0/1)
ShowMapSolid                   = 0                                   ### Show map collision solid mode (0/1/2)
MapTriCacheRecalc              = 0                                   ### Always recalc planes
MapCollisionBalance            = 12.000000                           ### Faces per quad balance
ShowInfoOnSectorError          = 0                                   ### show debug info on sector errors (0/1)
TXF_CheckFiles                 = 0                                   ### check .TXF files (0/1)
RadiosityMinDist               = 0.400000                            ### Min. distance between patches coef
RadiosityPortals               = 0                                   ### Use portals for radiosity (0/1)
RadSkipBySectors               = 0                                   ### Use sectors for radiosity (0/1)
LightmapLinealAtten            = 1                                   ### Use lineal attenuation for lightmap lights (0/1)
MapRenderMap                   =                                     ### Render only the specified materials (ie: wall*)
MapRenderMat                   =                                     ### Render only the specified materials (ie: wall*)
MapSortByShader                = 0                                   ### Sort by mat&shader (0/1)
MapDrawBySector                = 1                                   ### Draw map by sector (0/1)
MapDrawSector                  = -2                                  ### Draw only the specified sector (def. -2)
RenderSectors                  = 1                                   ### Render sectors (0/1)
RenderMap                      = 1                                   ### Render map (0/1)
R_ForceLMap                    = -1                                  ### Force primary/secondary lightmap (def. -1)
R_ParticlesCount               = 22892                               ### Particles Count
R_ParticleSector               = 1                                   ### Use sector visibility
R_ParticleFlags                = -1                                  ### Particle flags
R_ParticleScale                = 1.000000                            ### Particle scale
R_ParticleRate                 = 0                                   ### Particle rate
R_ParticleLife                 = 1.000000                            ### Particle life
R_ParticleVelScale             = 1.000000                            ### Particle velocity scale 1
R_Particles                    = 1                                   ### Transform & Show Particles (0/1)
R_FogAbsDist                   = 0                                   ### Fog range is in world coords (0/1)
R_FogDensity                   = 0.000000                            ### Force fog density (def. 0)
R_FogColor                     = -1                                  ### Force fog color (def. -1)
R_FogEnable                    = 1                                   ### Allow/disable fog (def. 1)
WorldPreIllum                  = 2                                   ### World static illum. (0=skip,1=normal,2=selfillum)
SkyTubeTest                    = 20000000.000000                     ### Sky tube test far plane
SkyRotation                    = 0.000000                            ### Sky rotation in degrees (Y-axis)
SkyPosScale                    = 1.000000                            ### Sky position scale
SkyZBuffer                     = 0                                   ### Sky requires ZBuffer
SkyInit                        = 1                                   ### Sky initialization
RenderSky                      = 1                                   ### Transform and render sky nodes
RenderWorld                    = 1                                   ### Transform and render world nodes
R_StencilLDir                  = 2000.000000                         ### Dir light shadow distance
R_StencilFisq                  = 0                                   ### Use fast inverse sqrt (0/1)
R_StencilBBox                  = 1                                   ### Discard by approx. object bbox (0/1)
R_StencilMult                  = 1.000000                            ### Stencil shadows distance mult
R_StencilTog                   = 0                                   ### Toggle stencil shadows
R_StencilSelf                  = 1                                   ### Self-proyected stencil shadows (0/1)
R_ShowStencil                  = 0                                   ### Show stencil shadows (0/1/2/3/4)
R_StencilShadows               = 1                                   ### Enable stencil shadows (req. reset3d) (-1/0/1)
R_LastDevice                   = NVIDIA GeForce GTX 1080 [nvldumd.dll]  27.21.14.6627    ### Render Last Device name
R_GlowFlickBRot                = 0.000000                            ### GlowFlick bump rot
R_GlowFlickBump                = 0.001500                            ### GlowFlick bump scale
R_GlowFlickRot                 = 0.100000                            ### GlowFlick rot
R_GlowFlickTile                = 6.000000                            ### GlowFlick tiling
R_GlowFlickMod                 = 0.980000                            ### GlowFlick mod coef
R_CloudEmi                     = 1.000000                            ### Cloud emissive factor
R_CloudA                       = 0.300000                            ### Cloud alpha factor
R_CloudB                       = 1.000000                            ### Cloud blue factor
R_CloudG                       = 1.000000                            ### Cloud green factor
R_CloudR                       = 1.000000                            ### Cloud red factor
R_CloudScale2                  = 3.000000                            ### Cloud scale 2
R_CloudScale1                  = 7.000000                            ### Cloud scale 1
R_CloudVel2y                   = 0.003000                            ### Cloud vy2
R_CloudVel2x                   = 0.020000                            ### Cloud vx2
R_CloudVel1y                   = 0.015000                            ### Cloud vy1
R_CloudVel1x                   = 0.005000                            ### Cloud vx1
R_AlphaFog                     = 1                                   ### Allow fog with alpha blending (0/1)
R_DecalZBias                   = 2                                   ### Z-Bias for decals (0..16)
R_CullMode                     = 0                                   ### Triangle culling mode (0=normal, 1=force two-sided)
R_MaterialLog                  = 0                                   ### Log material usage (0/1)
R_ShowSphereVis                = 0                                   ### Show sphere visibility tests (0/1/2)
R_UseDefMaterial               = 0                                   ### Use default white material (0/1)
R_UseDefTexture                = 1                                   ### Use default white texture (0/1/2)
R_MipFilter                    = 1                                   ### MipMap filter (0=point,1=linear)
R_TexFilter                    = 2                                   ### Texture filter (0=point,1=linear,2=anisotropic)
R_Anisotropy                   = 8                                   ### Max. anisotropic texture filter level
R_MipmapBias                   = 0.000000                            ### Mipmapping bias (def. 0.0)
R_EnvBumpScale                 = 1.000000                            ### Environment bump mapping scale
R_EnvBumpBias                  = 1                                   ### Adjust bias for DXT1 bump textures (0/1)
R_EnvMapOffset                 = 0.500000                            ### Environment map offset
R_EnvMapScale                  = 0.250000                            ### Environment map scale
R_EnvMapViewDep                = 2                                   ### View-dependent Environment map (0/1/2)
R_VBIBTriLimit                 = -1                                  ### RenderVBIB triangle limit (def. -1)
R_PShaderCount                 = 45                                  ### Count of pixel shader changes (readonly)
R_PSMask                       = 0                                   ### Pixel shader mask (def. 0)
R_PShaders                     = 1                                   ### Use pixel shaders (0/1)
R_GlowMap                      = 1                                   ### Use GlowMap (0/1)
R_EnvBump                      = 1                                   ### Use EnvBump (0/1)
R_EnvMap                       = 1                                   ### Use EnvMap (0/1)
R_EnvBlend                     = 0                                   ### MaskEnvMap blend mode (0=Add,1=Blend)
R_Tex_Count                    = 765                                 ### Texture counter
SaveDXT5                       = 1                                   ### Save DXT5 textures (0/1)
BumpDDS                        = 0                                   ### Allow compression of bump textures (0/1)
CachedTex                      = 20                                  ### Max. cached textures
MipmapColor                    = 0                                   ### Colorize each mipmap level (0/1)
MipmapFade                     = 0                                   ### Fadeout each mipmap level (0/1)
SharpenMore                    = 0                                   ### Extra sharpen for each mipmap level (0/1)
TextureLOD                     = 0                                   ### Most detailed mipmap level used (0=disable)
DUDVMipmap                     = 1                                   ### Allow mipmapping for DUDV textures (0/1)
BumpMipmap                     = 0                                   ### Allow mipmapping for bump textures (0/1)
BuildDDS                       = 0                                   ### Build DDS Textures (0/1)

EngineDebugLevel               = 2                                   ### Extra engine debug info (0/1/2)
S_StreamBufferSize             = 200                                 ### Buffer size for streaming (ms)
S_VoiceoverFadeout             = 2.000000                            ### Voiceover fadeout speed
S_VoiceoverFadein              = 4.000000                            ### Voiceover fadein speed
S_VoiceoverVolume              = 0.600000                            ### Voiceover relative volume
VSync                          = 1                                   ### Fullscreen Vertical Sync (0/1)
ShowTSCMode                    = 1                                   ### Show TSC info (0=instant,1=by seconds)
AutoScreenShot                 = 0                                   ### Auto ScreenShot (0/1)
R_ForceFPS                     = 0.000000                            ### FPS force (def. 0.0)
R_LimitFPS                     = 0.000000                            ### FPS limit (def. 0.0)
R_ShowInfo                     = 0                                   ### Show rendering info (0..3)
ShowSceneCamera                = 0                                   ### Show cutscene camera name and frame number
CameraDefViewAspect            = 1.333333                            ### Default logical viewport aspect ratio
PhysicalAspectRatio            = 1.333333                            ### Physical aspect ratio

R_SplitScreenUpdate            = 0                                   ### Split Screen Update Target
R_SplitScreenCamera            = 0                                   ### Split Screen Camera Index
R_SplitScreen                  = 0                                   ### Split Screen
R_CreditsAlpha                 = 0                                   ### Credits render target alpha
R_CreditsPhase                 = 0                                   ### Credits render target phase
R_CreditsClear                 = 1                                   ### Credits render target clear
R_CreditsY                     = 0                                   ### Position Y of Credits render target
R_CreditsX                     = 0                                   ### Position X of Credits render target
R_CreditsSizeY                 = 256                                 ### Size Y of Credits render target (pow2)
R_CreditsSizeX                 = 512                                 ### Size X of Credits render target (pow2)
R_CreditsRTarget               = 0                                   ### Init Credits render target (0/1)
R_SceneBlurOffset              = 1.500000                            ### Scene Blur Offset in Texels
R_SceneBlurValue               = 0.000000                            ### Scene Blur Value
R_SceneBlurRTarget             = 1                                   ### Init Scene Blur render target (0/1)
R_SceneRadialBlurOffset        = 5.000000                            ### Scene Radial Blur Offset
R_SceneRadialBlurValue         = 0.000000                            ### Scene Radial Blur Value
R_SceneRadialBlurRTarget       = 1                                   ### Init Scene Radial Blur render target (0/1)
R_SceneMotionBlurSize          = 0.500000                            ### Scene Motion Blur Target Size (Scene Size Proportional)
R_SceneMotionBlurOffset        = 1.000000                            ### Scene Motion Blur Offset in Texels
R_SceneMotionBlurOff           = 0.000000                            ### Scene Motion Blur OffScreen
R_SceneMotionBlurValue         = 0.000000                            ### Scene Motion Blur Value
R_SceneMotionBlurRTarget       = 0                                   ### Init Scene Motion Blur render target (0/1)
R_SceneBloomBlurSize           = 0.400000                            ### Scene Bloom Blur Target Size (Scene Size Proportional)
R_SceneBloomBlurOffset         = 0.750000                            ### Scene Bloom Blur Offset in Texels
R_SceneBloomBlurPasses         = 2                                   ### Scene Bloom Blur Passes
R_SceneBloomRTarget            = 0                                   ### Init Scene Bloom render target (0/1)
R_SceneDuDvCheckPixels         = 6553                                ### Scene DuDv Check Caps Maximun different Pixels
R_SceneDuDvForced              = 0                                   ### Scene DuDv Target Forced (0/1)
R_SceneDuDvPow2                = 0                                   ### Scene DuDv Pow2 Scene Copy
R_SceneDuDvScale               = 0.150000                            ### Scene DuDv Target Scale
R_SceneDuDvFilter              = 1                                   ### Scene DuDv Target Filter (0=point, 1=linear)
R_SceneDuDvRTarget             = 0                                   ### Init Scene DuDv render target (0/1)
R_SceneCheckPixels             = 512                                 ### Scene RenderTarget Caps Maximun different Pixels
R_SceneForceLinNonPow2         = -1                                  ### Force Linear NonPow2 Render Target (-1/0/1)
R_SceneForceLinPow2            = -1                                  ### Force Linear Pow2 Render Target (-1/0/1)
R_SceneRTargetSwap             = 1                                   ### Scene render target Swapping (0/1)
R_SceneRTarget                 = 1                                   ### Init Scene render target (0/1)
R_NewsPanelWire                = 0                                   ### Show the NewsPanel in wireframe mode (0/1)
R_NewsPanelSize                = 128                                 ### Size of NewsPanel render target (pow2)
R_NewsPanelRTarget             = 1                                   ### Init NewsPanel render target (0/1)
R_ForcePreRenderTransform      = 0                                   ### Force PreRender Transforms
R_GetModelVertex               = 1                                   ### Model GetVertex Active
R_CoefMLODMenuElement          = 11700.000000                        ### MenuElement LOD coef.
R_CoefMLODOutElement           = 80000.000000                        ### OutElement LOD coef.
R_CoefMLODCharacters           = 1500.000000                         ### Characters LOD coef.
R_CoefMLODTraffic              = 12000.000000                        ### Traffic LOD coef.
R_CoefMLODEngines              = 8000.000000                         ### Engines LOD coef.
R_CoefMLODPilots               = 4500.000000                         ### Pilots LOD coef.
R_CoefMLODShips                = 8000.000000                         ### Ships LOD coef.
c_sboxmult                     = 20.000000                           ### WorldSphereCollision box mult
c_sboxshow                     = 0                                   ### WorldSphereCollision box info
c_sbox                         = 1                                   ### WorldSphereCollision box cache enable
c_sld2                         = 10                                  ### WorldSphereCollisionSlide2D max. iter.
c_sldi                         = 10                                  ### WorldSphereCollisionSlide max. iter.
c_scts                         = 0                                   ### WorldSphereCollisionCheck use: 0=slide, 1=test
c_schk                         = 1                                   ### Detect WorldSphereCollisionCheck cases
c_caps                         = 1                                   ### Detect vertical WorldSphereCollisionTest cases
c_hold                         = 0                                   ### Freeze WorldSphereCollisionTest calls
c_iter                         = 0                                   ### 
ShowProgressBar                = 1                                   ### Show loading progress bar (0/1)
ProgressBar                    = 1775                                ### Progress bar reference value (def. 1000)
SplashScreenFade               = 400                                 ### Splash screens fade time
ShowSplashScreen               = 1                                   ### Show loading screen (0/1)
PlayVideo                      =                                     ### Video played at init.
TimerFreqMult                  = 1                                   ### Timer frequency multiplier (def. 1, disable QPF=0)
FullScreen                     = 0                                   ### 0 = Windowed mode, 1 = Fullscreen mode
VideoWidth                     = 1920                                ### Screen width
VideoHeight                    = 1080                                ### Screen height
VideoBPP                       = 32                                  ### Bits per pixel

CollisionEpsilon               = 1.000000                            ### Collision epsilon

ModelAmbient                   = 0                                   ### Extra ambient light for models (def. 0)
RenderUseVB                    = 1                                   ### Use Vertex Buffers (0/1)
RenderModels                   = 1                                   ### Render models (0/1)
ShowMapCollision               = 0                                   ### Show map collision planes (0/1)
RenderLightmap                 = 1                                   ### Render lightmap mode (0/1/2)
ShowMapWireFrame               = 0                                   ### Show map wireframe mode (0/1/2)

ViewerModel                    =                                     ### Model used in viewer mode
ViewerAnim                     =                                     ### Model animation used in viewer mode
ViewerModelOffsetY             = 0.000000                            ### Viewer model offset (Y axis)
ViewerFOV                      = 0.000000                            ### Viewer camera fov (0.0 = original fov)
ViewerClipFar                  = 800000.000000                       ### Viewer camera far clip plane
ViewerClipNear                 = 5.000000                            ### Viewer camera near clip plane
ViewerCameraInv                = 1                                   ### Viewer camera rotation: 0 = normal, 1 = inverted
ViewerCameraTgt                = 0                                   ### Viewer camera mode: 0 = free, 1 = target
ViewerCameraVel                = 1.000000                            ### Viewer camera velocity (m/s)

ViewerCameraAnim               = 0                                   ### Viewer camera anim (0/1)
LoadTextures                   = 1                                   ### Load textures (except Sprite2D ones) (0/1)
MatEmissive                    = 0.000000                            ### Extra amount of emissive lighting
DDS_CheckMark                  = 0                                   ### Check that used textures are not marked (0/1)
DDS_MarkSource                 = 0                                   ### Mark original texture (0/1)
DDS_UseTextures                = 1                                   ### Read DDS Textures (0/1)


LifeReachedCallback            = <Callback function>                 ### Life reached callback
LifeToLaunchCallback           = 30                                  ### Life to launch callback
RegenerationItem               = RegenerationBar                     ### Name of the bar item to make the regeneration
RegenerationCharTimeRate       = 1.000000                            ### between RegenerationTimeRate sec, 1 point regenerates.(char)
RegenerationCharStartTime      = 10.000000                           ### after this time, life´s regeneration starts.(char)
RegenerationTimeRate           = 0.100000                            ### between RegenerationTimeRate sec, 1 point regenerates.(ship)
RegenerationStartTime          = 3.000000                            ### after this time, life´s regeneration starts.(ship)


OnParkedOut                    = <Callback function>                 ### Callback when a occupied parking zone is free.


OnParkingOccupied              = <Callback function>                 ### Callback when a parking zone is occupied.
ParkingCheckRadius             = 500.000000                          ### Spere to check the position of the item or ship.
ParkingVehiCheckDistance       = 50000.000000                        ### At this distance, the parking will be check.
ParkingCharCheckDistance       = 15000.000000                        ### At this distance, the parking will be check.
OnMoneyReachValue              = 0                                   ### if money reach these vaule, the call OnMoneyReachCallback


OnMoneyReachCallback           = <Callback function>                 ### Function to be called when money reach 'OnMoneyReachValue'
StrMoneyUpdate                 = 0.100000                            ### Time to update the Money Scorer
PoliceTauntRace                = Police                              ### Taunting race (police, exept in GDB)
GuaranteedChars                =                                     ### List of not Forbidden  characters in a map.
 ','+char1+','+char2+','
UsrDefChar                     = Dtritus                             ### Standard main character type


AlarmCallback                  = <Callback function>                 ### The alarm Callback function.
AlarmGrowDelta                 = 0.045000                            ### The alarm status go up.
AlarmFallMission               = 1.200000                            ### The alarm status go down. (if outdoormap and mission)
AlarmFallDelta                 = -0.125000                           ### The alarm status go down.
EasyAlarmFallFactor            = 1.200000                            ### The alarm status go down multiplier for easy mode.
MaxChasingShips                = -1                                  ### Maximun number of chasing ships.
MaxTrafficEnemy                = 4                                   ### Maximun number of attaking traffic.
MinTrafficEnemyTime            = 1.000000                            ### Min Time attacking of traffic
MaxTrafficEnemyTime            = 30.000000                           ### Max Time attacking of traffic
MaxFightingTrafficSize         = 4.000000                            ### Max fighting traffic size
ProbTrafficFighting            = 100.000000                          ### Prob traffic fighting
TrafficFightingMaxDist         = 50000.000000                        ### Traffic fighting max dist
TrafficRemovalDist             = 100000.000000                       ### Traffic removal dist
TrafficDamageTolerance         = 10                                  ### Life Points to be your enemy
iTrafficNumber                 = 7                                   ### Sets the traffic on the sky
PlayerHelpedPoliceReward       = 2000                                ### Player helped police reward


OnPlayerHelpedPolice           = <Callback function>                 ### Called if player helped police


OnNeedMoreChasingTraffic       = <Callback function>                 ### Called if the chasing traffic is not enough


OnNeedMoreTraffic              = <Callback function>                 ### Called if the traffic is not enough
MadHuntersTriggeredShipName    =                                     ### Ship name that triggers mad hunters appearance
MosquitosTriggeredShipName     =                                     ### Ship name that triggers mosquitos appearance
MaxMadHuntersDist              = 70000.000000                        ### Max mad hunters dist
MaxMadHunters                  = 2                                   ### Max mad hunters
MaxMosquitosDist               = 30000.000000                        ### Max mosquitos dist
MaxMosquitos                   = 10                                  ### Max mosquitos
MinPercMadHuntersAttackingIntruder = 0.500000                            ### Min perc mad hunters attacking intruder
MinPercMosquitosAttackingIntruder = 0.300000                            ### Min perc mosquitos attacking intruder
OnMadHunterDeathMoney          = 300                                 ### Mad hunter death money reward
OnMosquitoDeathMoney           = 100                                 ### Mosquito death money reward
PhoneCabWarningDist            = 7000.000000                         ### PhoneCab warning dist (in meters).
TimeBetweeenWarnings           = 90.000000                           ### Time betweeen warnings.
TimeBetweeenTaunts2            = 15.000000                           ### Time betweeen taunts when the Boss controls all the robots.
TimeBetweeenTaunts             = 22.000000                           ### Time betweeen general taunts.


OnTaunt                        = <Callback function>                 ### Function to be called when a taunt is to be launched
DoResetOutPolice               = 0                                   ### if true, the police will be reset.


PoliceWaveEliminated           = <Callback function>                 ### Called if no police active in game.


OnDominFriendDeath             = <Callback function>                 ### Called when a friend dies
LeaderName                     =                                     ### Leader name


OnDominEnemyDeath              = <Callback function>                 ### Called when an enemy dies
DominFightingFreezeControlAim  = 6                                   ### Domin fighting freeze control aim
DominFightingFreezeCadenceShoot = 2                                   ### Domin fighting freeze cadence shoot
DominWithinRangeDist           = 20000.000000                        ### Domination within range dist
DominMinRangeDist              = 10000.000000                        ### Domination min range dist
DominMaxRangeDist              = 100000.000000                       ### Domination max range dist
MaxDominDistChase              = 5000.000000                         ### Max distance to zone objective in Domination mode.

MinDominDistChase              = 1500.000000                         ### Min distance to zone objective in Domination mode.

PercFriendsAttackLeaderWhenWinning = 0.500000                            ### CTFFriends percentage attacking leader when he's winning
LeaderFlag                     =                                     ### Leader flag
PercEnemiesAttackPlayerWhenWinning = 0.700000                            ### CTFEnemies percentage attacking player when he's winning
PlayerCTFTeamIsWinning         = 0                                   ### Is player's team winning the CTF?
GateKeeperStdFar               = 1000.000000                         ### Standard GateKeeper Distance of View
GateKeeperStdFovY              = 1.570796                            ### Standard GateKeeper FieldOfView
GateKeeperStdFovX              = 2.356194                            ### Standard GateKeeper FieldOfView
GateKeeperHiddenTime           = 5.000000                            ### Time iniside the shell of the gatekeeper when attacked


OnDefStateCallback             = <Callback function>                 ### Python function to be called when the NPC is forced to have the default state
GenCharSpecialChaseSpeed       = -1.000000                           ### Gen char special chase speed
GenCharPoliceRefuse            = 50.000000                           ### Percentage of times when the generic char escapes from the police
GenCharAcuseAgainTime          = 4.000000                            ### Time to acuse again after having received damage from the Gear (being acusing the main char)
GenCharAcuseTime               = 2.000000                            ### Minimal time pointing the main character
GenCharAttackLimit             = 2000.000000                         ### Beyond this distance the generic logic does not attack randomly!
GenCharStdFar                  = 800.000000                          ### Standard GenChar Distance of View
GenCharStdFovY                 = 1.570796                            ### Standard GenChar FieldOfViewY
GenCharStdFovX                 = 1.570796                            ### Standard GenChar FieldOfViewX
GenCharRobberyDetection        = 20.000000                           ### GenChar robery detection percentage
GenCharGetAwayTime             = 4.000000                            ### GenChar get away time
GenCharSpecialActionTime       = 15.000000                           ### GenChar special action time
GenCharMaxSpecialActionTime    = 12.000000                           ### GenChar max special action time
GenCharMinSpecialActionTime    = 6.000000                            ### GenChar min special action time
GenCharSpecialActionRadius     = 6250000.000000                      ### GenChar special action radius
GenCharAttackSpeed             = 0.800000                            ### GenChar speed (Attack)
GenCharEscapeSpeed             = 0.850000                            ### GenChar speed (Escape)
GenCharAlertSpeed              = 1.000000                            ### GenChar speed (Alert)
GenCharRelaxSpeed              = 0.400000                            ### GenChar speed (Relax)
GenCharAttackActive            = 1                                   ### if 1, the characters can attack.
PoliceBossMaxSpecialActionTime = 24.000000                           ### PoliceBoss max special action time
PoliceBossMinSpecialActionTime = 12.000000                           ### PoliceBoss min special action time
MainMissionStopDist            = 1500.000000                         ### Main mission stop dist
LittlePoliceChasingTime        = 3.000000                            ### Little police chasing time
LittlePoliceStopAcusingMaxDistFromUser = 4000.000000                         ### Little police stop acusing max dist from user
LittlePoliceMaxDistFar         = 1500.000000                         ### Little police max distance of view acusing
LittlePoliceAsksForMoney       = 1                                   ### Little police asks for money
GetAwayHumanDist               = 600.000000                          ### Get away human dist
BishopAttackOnAlarm            = 0                                   ### 1 if the bishop attack the player entity on alarm
BishopSpecialActionTime        = 5.000000                            ### Bishop special action time
BankDirectorAgressive          = 0                                   ### The bank director becomes more agressive (indoors)
MessengerGotoSpeed             = 0.350000                            ### Messenger speed when carry a tube or go for it.
MessengerDataPack              = MessengerDataPack                   ### Desktops functionary list name
MessengerDropPrice             = 500                                 ### The price if a messager drop the tube...


MessengerTakenCallback         = <Callback function>                 ### Called if a messager takes a datapack


MessengerDropCallback          = <Callback function>                 ### Called if a messager drop a datapack
MessengerPrepareDistance       = 1200.000000                         ### Distance to the objetive to prepare drop
MessengerObjetiveDistance      = 300.000000                          ### Distance to the objetive to drop...
MessengerTubeState             = 1                                   ### State of the tube : 0:Empty or 1:filled
MessengerDataPackMissionArrow  = 2                                   ### Type of indication of the 'Game of the messengers' mission.


OnFunctionaryStartsWorking     = <Callback function>                 ### Function to be called when a functionary sits down and starts working
FunctionaryAssignWorkDistance  = 600.000000                          ### Distance from the chair to reposisionate the functionary
FunctionarySpecialActionTime   = 1.500000                            ### Functionary special action time
FunctionarySpecialActionStatesTransitionTime = 0.500000                            ### Functionary special action states transition time
FunctionaryMaxtimeToStopWorking = 50.000000                           ### Functionary max time to get up
FunctionaryMintimeToStopWorking = 30.000000                           ### Functionary min time to get up
FunctionaryMaxTimeToSitDown    = 30.000000                           ### Functionary max time to sit down
FunctionaryMinTimeToSitDown    = 15.000000                           ### Functionary min time to sit down
RelaxSeatsFunctionaryListName  = RelaxSeatsFunctionary               ### Relax seats functionary list name
DesktopsFunctionaryListName    = DesktopsFunctionary                 ### Desktops functionary list name
SputnikJunyardTimeToPissPlayer = 60.000000                           ### SputnikJunyard time to piss player
PlatformRadiusSqr              = 1575025                             ### Platform radius squared
NumWorkingLoops                = 3                                   ### Num working loops
JunkPointsListName             = JunkPoints                          ### Junk points list name
MaintenanceSphereRadiusFactor  = 1.000000                            ### Maintenance sphere radius factor
MaintenanceTimeToNextPos       = 8.000000                            ### Maintenance time to next pos in cube
BossWalkingTime                = 30.000000                           ### Boss walking time
BossWorkingTime                = 60.000000                           ### Boss working time
BossWorkPlace                  =                                     ### Boss' work place dummy name
NursePoliceRefuse              = 50.000000                           ### percentage of times when the Nurse escapes from the police
NurseBankerDetect              = 30.000000                           ### percentage of times when the Nurse escapes from the banker
NurseEscapeTime                = 8.000000                            ### Nurse Escape Time
NurseAlertSpeed                = 1.000000                            ### Nurse speed (Alarm)
NurseRelaxSpeed                = 0.300000                            ### Nurse speed (Relax)
SecondaryMissionDesc           =                                     ### Secondary Mission Descriptor.
PrimaryMissionDesc             = Ich brauche einen Tapetenwechsel... Ich will andere Welten sehen!    ### Main Mission Descriptor.
NotCleanableByGear             =                                     ### Gear do not try to atack this
DefActionRadius                = 2500.000000                         ### Default action radius for characters logic
GearRageMaxTime                = 10.000000                           ### Time to get te rage and attack the stupid guys!
LogicAwakeTime                 = 90.000000                           ### Max time dazed for the logical managed characters.
SentinelBankerNPCDetect        = 50.000000                           ### percentage of times when the eye acuse the banker (for npcs)
SentinelBankerDetect           = 30.000000                           ### percentage of times when the eye acuse the banker
SentinelAbortyNPCAttDist       = 4000.000000                         ### At this distance, if not seen will abort the NPC attack
SentinelGotoSpeed              = 1.000000                            ### Sentinel speed (Goto order)
SentinelInspectSpeed           = 0.250000                            ### Sentinel speed (Inspect)
SentinelSuspectSpeed           = 0.500000                            ### Sentinel speed (Suspect)
SentinelAcuseSpeed             = 0.600000                            ### Sentinel speed (Acuse)
SentinelSearchSpeed            = 1.000000                            ### Sentinel speed (Search)
SentinelRelaxSpeed             = 0.250000                            ### Sentinel speed (Relax)
SentinelNextGotoTime           = 5.000000                            ### Sentinel time between goto orders.
SentinelGotoRadius             = 300.000000                          ### Radius to the viewpoint (Goto)
SentinelGotoTime               = 5.000000                            ### Time following the xtrange viewpoint (Goto)
SentinelInspectTime            = 3.000000                            ### Time following the main after out of viewrange (Inspect)
SentinelSuspectTime            = 3.000000                            ### Time following the main after out of viewrange (Suspect)
SentinelAcuseTime              = 3.000000                            ### Time following the main after out of viewrange (Acuse)
SentinelStdFar                 = 1000.000000                         ### Standard Sentinel Distance of View
SentinelStdFovY                = 1.570796                            ### Standard Sentinel FieldOfView
SentinelStdFovX                = 2.356194                            ### Standard Sentinel FieldOfView
PoliceLogicBelligerant         = 0                                   ### Must Be Initialized as 1 if Police Map


CreatePolice                   = <Callback function>                 ### This function is called if we need a Police


CreateGear                     = <Callback function>                 ### This function is called if we need a Gear
Gear2PoliceAlways              = 1                                   ### if 0 Gears will become polices only if no alarm
GearRobberyDetection           = 30.000000                           ### Gear robery detection percentage
GearAttackNPCTime              = 10.000000                           ### Time attacking an npc character
GearLostTargetTime             = 5.000000                            ### Time since the target got lost
GearScortSpeed                 = 0.500000                            ### Gear speed (Scort)
GearAttackSpeed                = 0.250000                            ### Gear speed (Attack)
GearChaseSpeed                 = 0.750000                            ### Gear speed (Chase)
GearRelaxSpeed                 = 0.500000                            ### Gear speed (Relax)
GearStdFar                     = 1500.000000                         ### Standard Gear Distance of View
GearStdFovY                    = 1.570796                            ### Standard Gear FieldOfView
GearStdFovX                    = 1.570796                            ### Standard Gear FieldOfView
DefInterpTime                  = 0.120000                            ### Interpolation value by default.
LogActEvents                   = 0                                   ### Drops to the console the log events.
ShowPathAI                     = 0                                   ### 0 = No Show, 1 = Show

TimeBetwChangeStateAI          = 0.050000                            ### Time between change state
NotShootAI                     = 0                                   ### 0 = Shoot AI, 1 = Not Shoot AI
ShowAI                         = 1                                   ### 0 = No Show, 1 = Show Inf. AI
AngleStrafeUnderAttackSentinelAI = 1.570796                            ### Angle of the opponent to strafe under attack.

TimeStrafeUnderAttackSentinelAI = 2.000000                            ### Angle of the opponent to strafe under attack sentinel.

LimVelRotDinamicMessengerAI    = 0.300000                            ### Lim. Vel. Rot. Dinamic Messenger.

VelRotDinamicMessengerAI       = 4.000000                            ### Vel. Rot. Dinamic Messenger.

TimeStrafeUnderAttackGearAI    = 3.000000                            ### Angle of the opponent to strafe under attack.

AngleStrafeUnderAttackGearAI   = 1.570796                            ### Angle of the opponent to strafe under attack.

TimeStrafeUnderAttackBishopAI  = 3.000000                            ### Angle of the opponent to strafe under attack.

AngleStrafeUnderAttackBishopAI = 1.570796                            ### Angle of the opponent to strafe under attack.

TimeStrafeLostObjCharAI        = 1.500000                            ### Time to do strafe when lost objective.

FactorDistTestColBackCharAI    = 1.500000                            ### Factor distance to check collision while backward.

FactorDistTestColCharAI        = 6.000000                            ### Factor distance to check collision.

TimeBetweenEventCollCharAI     = 5.000000                            ### Time between events  collision between agents.

TimeTestCollCharAI             = 0.000000                            ### Time to control time between tests collision between agents.

TimeStopCollCharAI             = 1.000000                            ### Time to control time between tests collision between agents when stopped.

TimeEventCollCharAI            = 1.000000                            ### Time to control event collision between agents.

MarginDetectCollCharAI         = 20.000000                           ### Margin to detect collision with characters.

MarginCollCharAI               = 5.000000                            ### Margin to test collision with characters.

MaxDistStopVisObjChaseWithOutActionAI = 1000.000000                         ### Max. distance stopped while is visible objective.

MaxDistStopVisObjChaseWithActionAI = 2000.000000                         ### Max. distance stopped while is visible objective.

MinDistStrafeCharAI            = 300.000000                          ### Min. distance to do while straffing.

MinAngleSearchPointCharAI      = 0.130900                            ### Angle to search point route.

DistNextPosGoTargetCharAI      = 305.000000                          ### Dist. to check new position to go.

NumPointsSearchSegmentCharAI   = 3                                   ### Num. Points to search point in segment.

OffsetAngOrientCharAI          = 0.049087                            ### Offset angle to final orient.

MaxRotCharAI                   = 7.500000                            ### Max. vel. rotation.

LimVelTurnCharAI               = 2.000000                            ### Limit velocity to turn.

DistShirkCharAI                = 0.100000                            ### Factor distance change shirk to move.

NameDebugShirkAI               =                                     ### Show info shirk agent.

ShowShirkAI                    = 0                                   ### Show info shirk.

ShowCharAI                     =                                     ### Show Features character.

OffsetMoveNurseAI              = 25.000000                           ### Offset to move Nurse.

DistActionNurseAI              = 1600.000000                         ### Distance to action the Nurse.

DistMaxShootMessengerAI        = 4000.000000                         ### Dist. Max. shooting Messenger.

TimeShootMessengerAI           = 1.000000                            ### Time shooting Messenger.

OffsetAngShootMessengerAI      = 1.570796                            ### Offset angle to shoot the Messenger.

ShootMessengerAI               = 2                                   ### Factor shoot Messenger.

OffsetAngShootGearAI           = 0.196350                            ### Offset angle to shoot the Gear.

ShootGearAI                    = 3                                   ### Factor shoot Gear.

MinTalkCharAI                  = 100.000000                          ### Min. diff. alt. to talk between two chars.

MinNumTalksCharAI              = 7                                   ### Time num. talks char.

MinTimeStoppedTurnPatrolCharAI = 5.000000                            ### Time min. duration turn to center of patrol char.

MinTimeStoppedCharAI           = 10.000000                           ### Time min. duration state intern stopped char.

MinTimeStopTempCharAI          = 30.000000                           ### Time min. duration state intern.

DistRadPauseCharAI             = 1000.000000                         ### Distance to radius of patrol to determine pause.

DistMaxCheckReposAI            = 5000.000000                         ### Distance max. to check repos.

DistMinCheckReposAI            = 1000.000000                         ### Distance to check repos.

DistMaxCheckPauseAI            = 15000.000000                        ### Distance max. to check pause.

DistMinCheckPauseAI            = 2000.000000                         ### Distance to check pause.

AngAttackBackCharAI            = 0.785398                            ### Angle to attack back.

MaxHeightChaseCharAI           = 300.000000                          ### Max height to chase.

DepthPathRouteInDoorAI         = 6                                   ### Depth Path in Route.

DistMaxShootBishopAI           = 4000.000000                         ### Dist. Max. shooting Bishop.

TimeShootBishopAI              = 2.000000                            ### Time shooting Bishop.

OffsetAngShootBishopAI         = 0.196350                            ### Offset angle to shoot the Bishop.

ShootBishopAI                  = 3                                   ### Factor shoot Bishop.

TimeChangeWeapCMAI             = 1.000000                            ### Time to change weapon CM.

TimeChangeWeapAI               = 10.000000                           ### Time to change weapon.

TimeShootCMAI                  = 0.500000                            ### Time Continue Shooting CM.

TimeShootAI                    = 1.000000                            ### Time Continue Shooting.

ShortDistShootAI               = 20000.000000                        ### Short Distance for weapons short distance.

MinDistCMAI                    = 30000.000000                        ### Distance min. use contrameasure.

OffsetAngShootAI               = 0.196350                            ### Offset angle to shoot.

ShowVehWeapAI                  =                                     ### Show Features Weapon vehicle.

ShowStopShipAI                 = 0                                   ### Info of agents stopped.
MinTimeReposAI                 = 0.050000                            ### Min. time to repos vehicle.

DecVelBrakeAI                  = 0.100000                            ### Dec. of velocity to brake.

MinAngleSearchPointAI          = 0.010000                            ### Angle to search point route.

DepthSearchPosGoAI             = 1                                   ### Depth to search inside segment fo path.

LimVelTurnObjectiveAI          = 1.000000                            ### Limit velocity to turn.

TimeReactTurnAI                = 2.000000                            ### Time reaction turn AI (in sec.).

DistBrakeObjAI                 = 10000.000000                        ### Distance brake to objective.

VelTurnAI                      = 1400.000000                         ### Velocity Min. to turn curves (cm/s).

DistBoostAI                    = 30000.000000                        ### Distance Min. to reactivate the Boost.

TimeMaxReachBoostAI            = 4.000000                            ### Time Max. to reach the objective to activate boost.

MaxRotAI                       = 20.000000                           ### Factor to control rotation.

MinRotAI                       = 2.000000                            ### Factor to control rotation.

ShowVehAI                      =                                     ### Show Features vehicle.



OnObjectiveNullAI              = <Callback function>                 ### Execute function in Python if objective is null


OnItemTakenAI                  = <Callback function>                 ### Execute function in Python to take item
VelTrafficLightRotAI           = 5556.000000                         ### Vel. traffic light to rotate.

VelReposStopAI                 = 7000.000000                         ### Vel. to repos agent back to camera.

VelReposBackAI                 = 3000.000000                         ### Vel. to repos agent back to camera.

RADIUS_OBJECTIVE_TRAFFIC_INDOOR = 4000.000000                         ### Radius Points Traffic InDoor.

RADIUS_OBJECTIVE_TRAFFIC       = 4000.000000                         ### Radius Points Traffic.

DimWindowReposYAI              = 20000.000000                        ### Dimension Y window to reposition agent.

DimWindowReposXAI              = 20000.000000                        ### Dimension X window to reposition agent.

MaxDistAroundReposAI           = 20000.000000                        ### Distance max. to reposition the agent around point of reposition.

MaxAngleReposAI                = 0.392699                            ### Angle max. to reposition the agent.

MaxMarginObjTrafficAI          = 1000.000000                         ### .

MinDistBetweenTrafficAI        = 5000.000000                         ### Distance Min. between two ships of traffic.

MaxDistChaseAI                 = 15000.000000                        ### Distance Max. to objective Chase AI.

MinDistChaseAI                 = 5000.000000                         ### Distance Min. to objective Chase AI.

MaxDistChaseElevatorAI         = 20000.000000                        ### Distance Max. to objective Chase AI inside hangar.

MinDistChaseElevatorAI         = 10000.000000                        ### Distance Min. to objective Chase AI inside hangar.

MaxDistElevatorAI              = 10000.000000                        ### Distance Max. to detect elevator near.

TimeDamageAI                   = 3.000000                            ### Time in sec. control damage.
DistGetAwayBoostAI             = 5000.000000                         ### Distance min. get away with boost.
DistNotGetAwayAI               = 45000.000000                        ### Distance not get away from enemy.
DistMinItemAI                  = 5000.000000                         ### Distance Min. for AI's purposes.
ShootAI                        = 0                                   ### 0 = AI cannot shoot, 1 = AI can shoot.
MinDistReposAI                 = 75000.000000                        ### Distance min. to reposition the agent.

MaxDistReposAI                 = 100000.000000                       ### Distance max. to reposition the agent.

MinDistReposStopAI             = 125000.000000                       ### Distance min. to reposition the agent when camera stopped.

MaxDistReposStopAI             = 150000.000000                       ### Distance max. to reposition the agent when camera stopped.

MinDistReposNotVisAI           = 37500.000000                        ### Distance min. to reposition the agent not visible.

MaxDistReposNotVisAI           = 75000.000000                        ### Distance max. to reposition the agent not visible.

DepthPathRouteOutDoorAI        = 6                                   ### Depth Path in Route.

AltPerpFloorAI                 = 20000.000000                        ### Alt. máx. to get point perp.

BatchBuildGraph2DAI            = 0                                   ### To Build Graph 2D.

ShowNodes2DAI                  = 0                                   ### 0 = No Show, 1 = Show Regions, 2 = Show Portals, 3 = Show Link's Portals, 4 = Show Portals + Links.
AltMinTestWalkAI               = 25.000000                           ### Alt. min. to test walk.

ShowTestCanGoAI                = 0                                   ### Show points to test can go to point.

ViewerIniAI                    = 0                                   ### To initialize AI in Viewer.

BatchBuildGraph3DAI            = 0                                   ### To Build Graph 3D.

ShowInfoRegAI                  = -1                                  ### Show info region when creation graph.

ShowNodesAI                    = 0                                   ### Show info graph.

RADIUS_OBJECTIVE_IN_ROUTE      = 4000.000000                         ### Radius Points Route.

RADIUS_SHIP_GRAPH              = 751.000000                          ### Radius Ship to Construct Graph.

DistGetPVisTrafficAI           = 200000.000000                       ### Distance máx. to repos traffic.

MaxNumTrackNormalDensityAI     = 15                                  ### Max. number of ships in track with normal density.

MaxNumTrackLowDensityAI        = 7                                   ### Max. number of ships in track with low density.

MinDistNodeTrafficAI           = 15000.000000                        ### Min. distance between nodes of traffic.

ShowNumTrafficAI               = 0                                   ### Show info traffic num.

ShowTrafficAI                  = 0                                   ### Show info traffic.

ShowAStarAI                    = 0                                   ### Show info AStar.

S_PlayMute                     =                                     ### Mute all sounds but those specified here
S_PitchScale                   = 1.000000                            ### Pitch scale (def. 1.0)
S_PriorityMode                 = 1                                   ### Priority mode (0=time,1=vol,2=time&vol)
S_SkipUpdates                  = 0                                   ### Disable sound updates (0/1)
S_SkipPlay                     = 0                                   ### Disable sound playing (0/1)
S_Show                         = 0                                   ### Show sound debug info on screen (0/1/2)
SoundInit                      = 1                                   ### Initialize sound system
SoundChannels                  = 24                                  ### Sound channels (max. 32)
SoundUseHardware               = 1                                   ### 0 = Software only, 1 = Use hardware if available
SoundSwapChannels              = 0                                   ### 0 = Normal, 1 = Swap left/right channels
SoundFrequency                 = 44100                               ### Frequency (11025/22050/44100)
SoundBits                      = 16                                  ### Bits (8/16)
SoundStereo                    = 1                                   ### 0 = Mono, 1 = Stereo

VoiceMainVolume                = 0.000000                            ### Voice main volume (0..1)
MusicMainVolume                = 0.000000                            ### Music main volume (0..1)
SoundMainVolume                = 0.000000                            ### Sound main volume (0..1)

StreamPath                     = Sounds/Stream/                      ### Stream default path
VoicePath                      = Sounds/Voices/                      ### Voice default path
SoundShowSetMode               = 0                                   ### Sound show SetMode info
SoundPanningFactor             = 12.000000                           ### Sound panning factor (dB)
SoundDistAttenuation           = 0.050000                            ### Sound distance attenuation factor
SoundDopplerLevel              = 1.000000                            ### Sound doppler effect level
SoundAutoplayVolume            = -60.000000                          ### Sound autoplay volume (dB)

WarnVoiceVolume                = 1.000000                            ### Voice maximal volume of police messages.

MaxPoliceWarnDist              = 3000.000000                         ### Distance of warnning police messages.

MinVoiceVolumeChat             = 0.200000                            ### voice minimal volume of thrd person speacher.

ForceNoActionMusic             = 0                                   ### Deactivates the action music.

useDynamicMusic                = 1                                   ### Uses dynamic music when set to true.

isActionIndoor                 = 0                                   ### True if the indoormap uses DinaMusic.

isActionMusic                  = 0                                   ### Modify this value to start/end the action!

MusicTimeChange                = 15.000000                           ### minimun time of musicplay after the fade.

ActionMusicTimeFade            = 5.000000                            ### Time to fade off the action musics.

OutActionMusicVolume           = 0.780000                            ### Volume of Action Music path for outdoors.

iOutActionMusic                = 11                                  ### Num of Action Music path for outdoors.

OutActionMusic                 = Music/Outdoor%d.ogg                 ### Action Music path for outdoors.

OutRelaxMusicVolume            = 1.000000                            ### Volume of Relax Music path for outdoors.

iOutRelaxMusic                 = 4                                   ### Num of Relax Music path for outdoors.

OutRelaxMusic                  = Music/Track%d.ogg                   ### Relax Music path for outdoors.

VoicePlayDelay                 = 0.500000                            ### Delay to play an specific voice.

WindFxScorerShow               = 0                                   ### Shows Wind FX info
WindFxScorerFwAngle            = 50.000000                           ### Foward angle Wind FX tests
WindFxScorerFadeFactor         = 5.000000                            ### Fade in and out for Wind FX
WindFxScorerVertical           = 5000.000000                         ### Vertical   check for Wind FX
WindFxScorerHorizontal         = 10000.000000                        ### Horizontal check for Wind FX
WindFxScorerSpeedPitch         = 7.000000                            ### semitones for speed
WindFxScorerSpeedVol           = 0.200000                            ### Sound Volume allways if speed factor
WindFxScorerSoundVol           = 0.300000                            ### Sound Volume for Wind FX
WindFxScorerSound              = FastFXWind                          ### Sound name for Wind FX
WeaponChangeFadeTime           = 0.100000                            ### Time to fade the fade Weapon Change Scorer
WeaponChangeShowTime           = 1.000000                            ### Time to show the fade Weapon Change Scorer
CurrentWaypointName2           =                                     ### Nombre de la siguiente boya en una carrera (Para el player 2)
CurrentWaypointName            =                                     ### Nombre de la siguiente boya en una carrera
FadeOutFinalTime               = 5.000000                            ### Fade out final time
CounterType                    = 0                                   ### Indica si se incrementa, se decrementa o se para el contador (0:decrementa, 1:incrementa, 2:se para)
TimeToFinishCurrentMission     = 0.000000                            ### Tiempo actual para que acabe la misión (en segundos)
TimeToCancelCurrentMission     = 21.000000                           ### Tiempo actual para cancelar la misión (en segundos)
TimeSpecialUseTimer            = 0.000000                            ### Temporizador definido por el usuario para usos varios.
TimeInactiveTimer              = 121.000000                          ### Tiempo actual para que se cancele la misión por inactividad (en segundos)
TimeWarning                    = 31.000000                           ### Cuando quede esta cantidad de tiempo se avisa al usuario de que se de prisa o se cancelará la apuesta loca (en segundos)
TextTypingSoundVol             = 0.200000                            ### Set the Text Typing Sound Volume
TextTypingSound                = keyboard%d                          ### Set the Text Typing Sound
EnemyFireSize                  = 2.000000                            ### The enemy fire indicator size
LittlePointingArrowSize        = 1.000000                            ### The little pointing arrow 0 : no arrow -> 1: normal -> oo
TargetScorerSwitchSoundVol     = 1.000000                            ### Sound Volume for switching target
TargetScorerSwitchSound        = SwitchTarget                        ### Sound name for switching target
FullTalkTime                   = 0.000000                            ### Time remain to dispear the tex showed...
RemainTalkTime                 = 0.000000                            ### Time remain to dispear the tex showed...
MaxTalkLineSizePix             = 225.000000                          ### Size at chat window with the text....
TimeToAbortChatText            = 0.500000                            ### This time must be keeped press the action button to abort the current chat.
FileArrowNextAlpha             = 2D/Dialog/NextOption.alpha.tga      ### FileArrowNextAlpha bitmap file
EndRegenerationSoundVol        = 0.300000                            ### Sound Volume for life end Regeneration
EndRegenerationSound           = EndRegeneration                     ### Sound for life end Regeneration
InitRegenerationSoundVol       = 0.500000                            ### Sound Volume for life initilaize Regeneration
InitRegenerationSound          = InitRegeneration                    ### Sound for life initilaize Regeneration
RegenerationSoundPitchMax      = 10.000000                           ### Full life pitch for life Regeneration
RegenerationSoundPitchMin      = -10.000000                          ### 0 life pitch for life Regeneration
RegenerationSoundVol           = 0.400000                            ### Sound Volume for life Regeneration
RegenerationSound              = Regeneration                        ### Sound loop for life Regeneration
DangerLifeSoundVol             = 0.300000                            ### Sound Volume for life danger
DangerLifeSound                = LifeDanger                          ### Sound loop for life danger
DangerLifeLevel                = 10                                  ### Percentage of life to show Danger...
WarningLifeLevel               = 25                                  ### Percentage of life to show Warning...
SpecialActionActive            = 2                                   ### the special action status. 0-Disable 1-Blink 2-Enable
GearTargetName                 =                                     ### Gear target entity name
GearTargetSphereRadius         = 3000.000000                         ### Gear target sphere radius
GearTargetCrossBlinkTime       = 0.100000                            ### Gear target cross blink time
ShowConsoleLog                 = 1                                   ### 1 to show allways the console


FullScreenConsoleCallback      = <Callback function>                 ### This function is called when imput an string on fullscreen console.
HintAppearsTime                = 0.500000                            ### Time to show the hint in the menu
XboxSavingMsgStr               = XBox_Saving_Msg_                    ### the remain 'Saving...' text message in language table.
XboxSavingMsg                  = 0.000000                            ### the remain time to hide de 'Saving...' message.
XboxNoPadMsgP                  = 0                                   ### if 1 shows the 'please insert the pad' for player 2.
XboxNoPadMsg                   = 0                                   ### if 1 shows the 'please insert the pad'.
XboxNoPadMsgPBig               = 0                                   ### if 1 shows the 'please insert the pad' big (to start game).
XboxNoPadMsgBig                = 0                                   ### if 1 shows the 'please insert the pad' big (to start game).
CameraCloudBlue                = 0                                   ### Blue falue for the clouds
CameraCloudGreen               = 60                                  ### Green falue for the clouds
CameraCloudRed                 = 120                                 ### Red falue for the clouds
CameraCloudAlpha               = 240                                 ### Aplha falue for the clouds
CameraCloudThickness           = 1000.000000                         ### The thickness of the cloud fade for de clouds
CameraCloudPlaneSize           = 1000.000000                         ### The size of de gradient of the fade for de clouds
CameraCloudDistance            = 2000.000000                         ### here start the white fade for de clouds
MotionBlurOffVar               = 0.000000                            ### factor of motion blur fx
MotionBlurEndTime              = 0.000000                            ### factor of motion blur fx
MotionBlurTime                 = 0.000000                            ### factor of motion blur fx
MotionBlurFactorEnd            = 0.000000                            ### factor of motion blur fx
MotionBlurFactorBegin          = 0.000000                            ### factor of motion blur fx
NoiseEndTime                   = 0.000000                            ### factor of noise fx
NoiseTime                      = 0.000000                            ### factor of noise fx
NoiseFactor                    = 0                                   ### factor of noise fx
NoiseFactorBegin               = 0                                   ### factor of noise fx
CinemaBlackBandHeight          = 60.000000                           ### Modifies the cinema format
ScorerMarkerSpeed              = 6.000000                            ### Scorer Focus Marker Speed
ScorerMarkerColor              = 11853055                            ### Scorer Focus Marker Color
ScorerMarker                   = 1                                   ### Show Scorer Focus Marker
ScorerMarginV                  = 10                                  ### Vertical Margin for Scorer
ScorerMarginH                  = 12                                  ### Horizontal Margin for Scorer
OnAcceptSoundVol               = 0.500000                            ### Set the Accept sound Volume
OnAcceptSound                  = menuclik                            ### Set the Accept Sound
OnFocusSoundVol                = 0.500000                            ### Set Volume in the focus of sound
OnFocusSound                   = menufocus                           ### Set the Focus Sound
CShow                          = 0                                   ### Shows the colission areas
SuperDealAvaliable             = 0                                   ### 1 if superdeal is avaliable
NumEnemiesInRadar              = 0                                   ### Number of enemies in the radar
RadarMMSelect                  = 1                                   ### 1 if Show only one main mission target (nearest)
RadarShowAll                   = 0                                   ### Show all the vehicles and chars at the radar
NumRadarIcons                  = 9                                   ### The number of radar icons
FileNameMap2D                  = Levels/Outskirts/2D/Map2D.tga       ### 2DMap bitmap file
NewsPanelCloseSpeed            = 4.000000                            ### Speed of close of scene
NewsPanelOpenSpeed             = 3.000000                            ### Speed of init of scene
NewsPanelH                     = 180.000000                          ### render the News Logo Size
NewsPanelW                     = 270.000000                          ### render the News Logo Size
NewsPanelY                     = 20.000000                           ### render the News Logo Pos
NewsPanelX                     = 350.000000                          ### render the News Logo Pos.
NewsPanelMove                  = 18.000000                           ### render the News Panel Head movement.
NewsPanelDisplacement          = 5.000000                            ### render the News Panel Head displacement.
NewsPanelDistance              = 70.000000                           ### render the News Panel Head distance.
NewsHead                       = Betty                               ### Render the News Head
BackNewsBmp                    = 2D/News/BackNews.bmp                ### render the News Background
NewsLogoBmp                    = 2D/News/LogoNews.bmp                ### render the News Logo
NewsPanelAspect                = 1.330000                            ### News Panel aspect ratio
NewsPanelShowHead              = 0                                   ### render the News Panel Head.
NewsPanelActive                = 0                                   ### render the News Panel in the texture.
ShowNetStatus                  = 1                                   ### true if show the networking status.

ShowClientPing                 = 0                                   ### true if show the ping label
ClientPingX                    = 20.000000                           ### X Pos of the ping label
ClientPingY                    = 120.000000                          ### Y Pos of the ping label.

FirstPhotoMessage              =                                     ### Message that appears every time you must to use the camere
NextMissionSecondLineOffsetXBox = 24.000000                           ### Next mission second line offset XBox
NextMissionFirstLineOffsetXBox = 4.000000                            ### Next mission first line offset XBox
NextMissionSecondLineOffsetPC  = 80.000000                           ### Next mission second line offset PC
NextMissionFirstLineOffsetPC   = 60.000000                           ### Next mission first line offset PC
ChatMsgPersistence             = 1.000000                            ### Time that will be printed the chat message
QuickMessageString1            = Die bastard!                        ### Quick chat messsage
QuickMessageString2            = This map sucks                      ### Quick chat messsage
QuickMessageString3            = Good game                           ### Quick chat messsage
QuickMessageString4            = Thatï¿½s no fair                    ### Quick chat messsage
QuickMessageString5            = There is no rules                   ### Quick chat messsage
QuickMessageString6            = Iï¿½m the one and only              ### Quick chat messsage

CannonScorerColorBlue          = 174                                 ### Cannon Color Blue
CannonScorerColorGreen         = 241                                 ### Cannon Color Green
CannonScorerColorRed           = 251                                 ### Cannon Color Red
CannonScorerNoAmmoSoundVol     = 1.000000                            ### Sound Volume for No Ammo Signal
CannonScorerNoAmmoSound        = NoAmmo                              ### Sound name for No Ammo Signal
IsAutoUpdatable                = 0                                   ### 
AutoUpdateSpeedFactor          = 1.000000                            ### 
AutoUpdateStopValue            = 0.000000                            ### 
BarValue                       = 0.000000                            ### 
BlinkTime                      = 0.100000                            ### Blink time


OnFinishAutoUpdate             = <Callback function>                 ### Called on finished auto update
MissionScorerName              = Mission                             ### Mission scorer name
TimeToMsg                      = 0.000000                            ### Tiempo restante hasta que desaparezca el mensaje
ServerDataRateLimit            = 20480                               ### Rate Limit in bytes per second



MasterCommandFunc              = <Callback function>                 ### MasterCommandFunc(string) (master server sends data)
HeartbeatTime                  = 60.000000                           ### Heartbeat to the master server.

MasterServerAddress            = 127.0.0.1                           ### Master server address for internet.
MasterServerPort               = 3666                                ### Master server port for internet. (0 = No master) 



OnNetBrowseCallback            = <Callback function>                 ### Called every time that server is found in a browsing operation.


OnChatString                   = <Callback function>                 ### OnChatString(UsrId,UsrString) UsrId is the number id ('net'UsrId)


OnUsrString                    = <Callback function>                 ### OnUsrString(UsrId,UsrString) UsrId is the number id ('net'UsrId)
ClientConectionStatus          =                                     ### String with conection information

ServerMinSendDelay             = 5                                   ### Mininimal delay between packets (in seconds).


OnClientModify                 = <Callback function>                 ### OnClientModify(entityname,ModelName,MaxLife,UsrName,PilotName,Motor0,Motor1,Motor2,Motor3,WeaponBay,tgtype) player ship modified


OnClientJoin                   = <Callback function>                 ### OnClientJoin(entityname,ModelName,MaxLife,UsrName,PilotName,Motor0,Motor1,Motor2,Motor3,WeaponBay,tgtype) player ship created


OnClientExit                   = <Callback function>                 ### OnClientExit(entityname,ModelName,UsrName) player ship will be deleted
ServerName                     = Unnamed Server                      ### Name of the network server

ForceServerVehicle             = 0                                   ### All the ships will use the server's one

ClientPPS                      = 20                                  ### Number of packets per second that will be send/request to the server [1..20]



ClientSetConfig                = <Callback function>                 ### ClientSetConfig(entityname,ModelName,MaxLife,UsrName,PilotName,Motor0,Motor1,Motor2,Motor3,WeaponBay,tgtype) player ship modifed


ClientSetPlayer                = <Callback function>                 ### ClientSetPlayer(EntityName)


ClientAfterCreate              = <Callback function>                 ### ClientAfterCreate(EntityName,ResoruceName)


ClientCreate                   = <Callback function>                 ### ClientCreate(EntityName,ResoruceName)


ClientDelRes                   = <Callback function>                 ### ClientDelRes(Num,Descriptor)


ClientAddRes                   = <Callback function>                 ### ClientAddRes(Num,Descriptor)
NetMaxPlayersInitSend          = 4                                   ### Maximun number of net players send per packet at the startup.
NetTimeOut                     = 240000                              ### # Time out for desconection...
NetMaxResourcesSend            = 8                                   ### Maximun number of net resourses send per packet at the startup.
ASEPublic                      = 1                                   ### 'The All-Seeing Eye' server public.



OnGeneralDamage                = <Callback function>                 ### Función callback de daño de propósito general
StdMaxLife                     = 100                                 ### Standard max life for characters and soon.
ActiveExtrapolation            = 0                                   ### 1 Uses Extrapolation if possible, 0 Uses Interpolation allways
MssnRadarBlinkTime             = 5.000000                            ### Time blinking if the new mission is assigned.
NetItemDistAct                 = 8000.000000                         ### Distance in cm to actualize the item data.
FXItemFadeMaxDist              = 60000.000000                        ### Maximun Distance to show the Item Fade Effect
FXVehicleProbeLight_SizeMax    = 8.000000                            ### Vehicle Police Siren FX Max Size (Mult)
FXVehicleProbeLight_SizeMin    = 2.000000                            ### Vehicle Police Siren FX Min Size (Mult)
FXVehicleProbeLight_DistGrow   = 4000.000000                         ### Vehicle Police Siren FX Distance for Grow
FXVehicleSiren_SizeMax         = 30.000000                           ### Vehicle Police Siren FX Max Size (Mult)
FXVehicleSiren_SizeMin         = 3.000000                            ### Vehicle Police Siren FX Min Size (Mult)
FXVehicleSiren_DistGrow        = 1500.000000                         ### Vehicle Police Siren FX Distance for Grow
FXTrafficEmbeddedFile          = Models/GFX/TrafficEmbeddedFX.M3D    ### Default Model for Traffic Embedded Effects
FXVehicleEmbeddedFile          = Models/GFX/VehicleEmbeddedFX.M3D    ### Default Model for Vehicle Embedded Effects
FXBossShieldAspect             = 0.500000                            ### 
FXBossShieldScale              = 1.500000                            ### 
FXBossShieldRadius             = 600.000000                          ### 
DataPackInterTime              = 0.600000                            ### DataPack Interpolate Status Time
DataPackLaserLong              = 225.000000                          ### DataPack Long of the Laser
DataPackLaserSize              = 8.000000                            ### DataPack Size of the Laser
MessengerLightingDist          = 2000.000000                         ### Max Distance to show Messenger Lighting Effects
FXRustyChispasSoundVol         = 1.000000                            ### Rusty efecto de chispas sound volume
FXRustyChispasSound            = FXRustyChispasSound                 ### Rusty efecto de chispas sound name
SentinelLaserScanerDist        = 4500.000000                         ### Max Distance to show Sentinel Laser Scaner
SndLoopCharNPCMul              = 2.500000                            ### Multiplicador de volumen para los loops de los npcs
FallSoundVel                   = 600.000000                          ### Beyond this fallspeed, the fallsound will run...
TimeToAbortSelectChar          = 30.000000                           ### Time to call AbortSelectFunc in chars if inactive.
CharProcessReduction           = 2000.000000                         ### Beyon this distance, the processing speed will be reduced if no visible.
EnergyBarActive                = 0                                   ### if 0, the energy bar action is disable.
CharUsrPushSpeed               = 100.000000                          ### Speed in cm/seg used to push characters....
AbortSelectDistance            = 1500.000000                         ### At this distance (from the center), the selection must be reseted.
EnergyRechargeTime             = 15.000000                           ### Time to recharge the full energy...
CharGrav                       = 3000.000000                         ### Characters Gravity.
AlwaysRun                      = 1                                   ### 1 allways run, 0 allways walk.
WalkCameraCenter               = 0.000000                            ### 0 is none else is the time to back to the standard view.

PadTurnSpeed                   = 1.000000                            ### Aditional rotation for pad controllers.

FXSebastianFlashFile           = Models/GFX/Sebastian/Flash.M3D      ### Default Model for Sebastian Flash Effect
RustyHitPosZ                   = -135.000000                         ### Rusty Hit Displacement from center
RustyHitPosY                   = -65.000000                          ### Rusty Hit Displacement from center
RustyHitPosX                   = -50.000000                          ### Rusty Hit Displacement from center
FXRustyHitFile                 = Models/GFX/Rusty/Hit.M3D            ### Default Model for Rusty Hit Effect
PoliceBossBrupBounceSoundVol   = 0.000000                            ### Police Boss Brup debris bounce sound volume
PoliceBossBrupBounce2Sound     = PoliceBossBrupBounce2Sound          ### Police Boss Brup debris bounce sound2 name
PoliceBossBrupBounce1Sound     = PoliceBossBrupBounce1Sound          ### Police Boss Brup debris bounce sound1 name
PoliceBossBrupDebrisMax        = 8                                   ### Police Boss Brup Max debris number
PoliceBossBrupDebrisMin        = 4                                   ### Police Boss Brup Min debris number
PoliceBossBrupDirRand          = 0.150000                            ### Police Boss Brup Random Direction factor
PoliceBossBrupPosZ             = -100.000000                         ### Police Boss Brup Displacement from center
PoliceBossBrupPosY             = 5.000000                            ### Police Boss Brup Displacement from center
PoliceBossBrupPosX             = 5.000000                            ### Police Boss Brup Displacement from center
PoliceBossBrupBaseFile         = Models/Misc/NutsAndScrew/NutsAndScrew    ### Default Model for Police Boss Brup Effect
PoliceBossActionRadius         = 1000.000000                         ### Radius of PoliceBoss fun FX to the polices.
FXPoliceGearConversionFile     = Models/GFX/Police/Conversion.M3D    ### Default Model for Police Gear Conversion Effect
FXPoliceStealFile              = Models/GFX/Police/PoliceSteal.M3D    ### Default Model for Police Steal Effect
PoliceAlarmStepSTM             = 0.100000                            ### Police Alarm Step in any Show Me The Money Action.
PoliceStealQuanto              = 10                                  ### Money stealed by the banker to the main player
NurseAlarmHit                  = 0.250000                            ### How values must increment when nurse hits
NurseDispRad                   = 75.000000                           ### Nurse hit detector Radius
NurseDispDist                  = 120.000000                          ### Nurse hit detector displacement distance
FXHammerHitFile                = Models/GFX/Nurse/HammerHit.M3D      ### Default Model for Nurse Hammer Hit Effect


OnSleep                        = <Callback function>                 ### Function to be called when the the player, as a nurse, sleeps someone
MessengerTakeDataPackSoundVol  = 1.000000                            ### Messenger Take DataPack sound volume
MessengerTakeDataPackSound     = MessengerTakeDataPack               ### Messenger Take DataPack sound name
MessengerShootSoundVol         = 1.000000                            ### Messenger shoot impact sound volume
MessengerShootSound            = MessengerShoot                      ### Messenger shoot impact sound name
MessengerAttackPosZ            = -40.000000                          ### Messenger Attack Displacement from center
MessengerAttackPosY            = -25.000000                          ### Messenger Attack Displacement from center
MessengerAttackPosX            = 0.000000                            ### Messenger Attack Displacement from center
FXMessengerTakeDataPackFile    = Models/GFX/Messenger/TakeDataPack.M3D    ### Default Model for Messenger Take DataPack Effects
FXMessengerAttackFile          = Models/GFX/Messenger/Attack.M3D     ### Default Model for Messenger Attack Effects
MessengerAmmoCost              = 0.050000                            ### Messenger AmmoCost Per shoot
FXMercenaryDrinkFile           = Models/GFX/Mercenary/Drink.M3D      ### Default Model for Mercenary Drink Effects
FXMercenaryDrinkSmokeFile      = Models/GFX/Mercenary/DrinkSmoke.M3D    ### Default Model for Mercenary Drink Smoke Effects
MercenaryDrinkPosZ             = 28.000000                           ### Mercenary Drink Displacement Z from center
MercenaryDrinkPosY             = 2.000000                            ### Mercenary Drink Displacement Y from center
MercenaryDrinkPosX             = 14.000000                           ### Mercenary Drink Displacement X from center
MayorSleepPercent              = 20.000000                           ### Sleep when listen probability
MayorListenPercent             = 50.000000                           ### Listen percent probability
MayorBlabliblaRadius           = 1000.000000                         ### Radius of Mayor´s Bla-Blas.
FXMaintenanceWorkFile          = Models/GFX/Maintenance/Work.M3D     ### Default Model for Maintenance Robot Work Effects
MaintenanceWorkSoundAttEnd     = 0.000000                            ### Maintenance Work sound attend
MaintenanceWorkSoundAttIni     = 0.000000                            ### Maintenance Work sound attini
MaintenanceWorkSoundVol        = 0.800000                            ### Maintenance Work sound volume
MaintenanceWorkSound           = MaintenanceWorkSound                ### Maintenance Work sound name


OnFlash                        = <Callback function>                 ### Function to be called when the the player, flash someone
GearLowWeaponEnergy            = 0.130000                            ### Gear low weapon energy value (between 0 and 1)
GearMissileSpeed               = 2500.000000                         ### Gear missile speed
FXGearMissileFile              = Models/GFX/Gear/Missile.M3D         ### Default Model for Gear Missile Effect
GearXplodeRadius               = 250.000000                          ### Radius of Gear's electric ball explosion.
GearShootPosZ                  = -180.000000                         ### Gear shoot Displacement from center
GearShootPosY                  = -45.000000                          ### Gear shoot Displacement from center
GearShootPosX                  = -50.000000                          ### Gear shoot Displacement from center
GearMissileThunderSoundVol     = 1.000000                            ### Gear missile thunder sound volume
GearMissileThunder2Sound       = GearMissileThunder2                 ### Gear missile thunder 2 sound name
GearMissileThunder1Sound       = GearMissileThunder1                 ### Gear missile thunder 1 sound name
GearMissileSoundVol            = 1.000000                            ### Gear missile loop volume
GearMissileSound               = GearMissile                         ### Gear missile loop name
GearHitSoundVol                = 1.000000                            ### Gear hit impact sound volume
GearHitSound                   = GearHit                             ### Gear hit impact sound name
GearShootSoundVol              = 1.000000                            ### Gear Shoot impact sound volume
GearShootSound                 = GearBoom                            ### Gear Shoot impact sound name
GearLoadWeaponSoundVol         = 1.000000                            ### Gear Load Weapon sound volume
GearLoadWeaponSound            = GearLoadWeapon                      ### Gear Load Weapon sound name
GearShootHitAlarm              = 0.150000                            ### The amount that will grow up if a shoot hits...
GearShootFailAlarm             = 0.100000                            ### The amount that will grow up if a shoot fails...
GearShootDistance              = 20000.000000                        ### Range in the Armored Gear weapon
GearShootDamage                = 13                                  ### Damage by the Armored Gear weapon
FunctionaryEffectFastSoundVol  = 0.400000                            ### Functionary Fast Effect sound volume
FunctionaryEffectFastSound     = effectfast                          ### Functionary Fast Effect sound name
FunctionarySpecialActionLow    = 0.150000                            ### Functionary special action low value (between 0 and 1)
DTritusHitTimeFader            = 0.200000                            ### DTritus Effect Time
DTritusHitTimeSpeed            = 0.050000                            ### DTritus Effect Time
FXDTritusKillFile              = Models/GFX/DTritus/Kill.M3D         ### Default Model for DTritus Kill Effect
FXDTritusAttackFile            = Models/GFX/DTritus/Attack.M3D       ### Default Model for DTritus Attack Effect
FXDesktopFallEndDist           = 10000.000000                        ### Max Distance to show Desktop Fall End Effect
FXDesktopFallEndFile           = Models/GFX/Desktop/FallEnd.M3D      ### Default Model for Desktop Fall End Effect
DesktopJumpSlideTime           = 0.500000                            ### Sliding time to jump again.
DesktopJumpPrice               = 5                                   ### if desktop jump over any character, the price of money is...
DesktopJumpSpeed               = 1000.000000                         ### Jump speed in cm/sec
BishopHitSoundVol              = 0.170000                            ### Bishop hit impact sound volume
BishopHitSound                 = BishopHit                           ### Bishop hit impact sound name
BishopShootSoundVol            = 0.140000                            ### Bishop shoot impact sound volume
BishopShootSound               = BishopShoot3                        ### Bishop shoot impact sound name
BishopAttackRandOff            = 50.000000                           ### Bishop Attack Random Offset from center
BishopAttackPosZ               = -135.000000                         ### Bishop Attack Displacement from center
BishopAttackPosY               = 25.000000                           ### Bishop Attack Displacement from center
BishopAttackPosX               = -15.000000                          ### Bishop Attack Displacement from center
FXBishopAttackFile             = Models/GFX/Bishop/Attack.M3D        ### Default Model for Bishop Attack Effects
FXBishopSellLifeFile           = Models/GFX/Bishop/SellLife.M3D      ### Default Model for Bishop Sell Life Effects
BishopAngleVariation           = 60.000000                           ### Angle of Randominzation of the shoot impulse
BishopAmmoCost                 = 0.025000                            ### Bishop AmmoCost Per shoot
BishopWeaponDamage             = 8                                   ### Bishop damage per hit that make the bishop
BishopLivePrice                = 1000                                ### Bishop live price
MaxPlayerLives                 = 50                                  ### Max player lives
BettyHSpeed                    = 1.100000                            ### Betty Speed Rotation (Horizontal)
BettyVSpeed                    = 1.100000                            ### Betty Speed Rotation (Vertical)
BettyHitPosZ                   = -65.000000                          ### Betty Hit Displacement from center
BettyHitPosY                   = -120.000000                         ### Betty Hit Displacement from center
BettyHitPosX                   = 20.000000                           ### Betty Hit Displacement from center
FXBettyKillFile                = Models/GFX/Betty/Kill.M3D           ### Default Model for Betty Kill Effect
FXBettyAttackFile              = Models/GFX/Betty/Attack.M3D         ### Default Model for Betty Attack Effect
BettyHitTopLimit               = 300.000000                          ### Betty Hit Top Limit (Y)
BettyHitRadius                 = 1000.000000                         ### Betty Hit Radius
BettyHitTimeFader              = 0.250000                            ### Betty Effect Time
BettyHitTimeSpeed              = 0.350000                            ### Betty Effect Time
BertoFlashSoundVol             = 0.600000                            ### Berto Flash sound volume
BertoFlashSound                = Flash2                              ### Berto Flash sound name
FXBertoFlashFile               = Models/GFX/Berto/Flash.M3D          ### Default Model for Berto Flash Effect
FXBertoAttackFile              = Models/GFX/Berto/Attack.M3D         ### Default Model for Berto Attack Effect
BertoFlashDist                 = 400.000000                          ### Berto Flash Max Distance
BertoAmmoCost                  = 0.030000                            ### Berto AmmoCost Per shoot
BankMasterBatonPosZ            = -85.000000                          ### BankMaster Baton Displacement from center
BankMasterBatonPosY            = 35.000000                           ### BankMaster Baton Displacement from center
BankMasterBatonPosX            = 0.000000                            ### BankMaster Baton Displacement from center
FXBankMasterSuctionFile        = Models/GFX/BankMaster/Suction.M3D    ### Default Model for BankMaster Suction Effect
FXBankMasterAttackFile         = Models/GFX/BankMaster/Attack.M3D    ### Default Model for BankMaster Attack Effect
BankMasterVacumDist            = 1000.000000                         ### BankMaster Flash Max Distance
BankMasterAmmoCost             = 0.050000                            ### BankMaster AmmoCost Per shoot
FXBankerStealFile              = Models/GFX/BankDirector/BankerSteal.M3D    ### Default Model for Banker Steal Effect
BankerStealSoundVol            = 0.200000                            ### Banker Steal sound volume
BankerSteal3Sound              = pasada-billete3-bank                ### Banker Steal sound name
BankerSteal2Sound              = pasada-billete2-bank                ### Banker Steal sound name
BankerSteal1Sound              = pasada-billete1-bank                ### Banker Steal sound name
BankerStealPosZ                = -60.000000                          ### Banker Steal Displacement from center
BankerStealPosY                = 10.000000                           ### Banker Steal Displacement from center
BankerStealPosX                = -50.000000                          ### Banker Steal Displacement from center
BankerStealQuanto              = 30                                  ### Money stealed by the banker to the main player
WeapHitClientResetTime         = 1.000000                            ### Tolerance to reset the values of the queue of hits to the client

FXArrowIndicatorFlash_SizeMax  = 6.000000                            ### Arrow Indicator Flash FX Max Size (Mult)
FXArrowIndicatorFlash_SizeMin  = 2.500000                            ### Arrow Indicator Flash FX Min Size (Mult)
FXArrowIndicatorFlash_DistGrow = 6500.000000                         ### Arrow Indicator Flash FX Distance for Grow
ArrowActiveHorizontal          = 100.000000                          ### The Horizontal distance betweem the both spheres
ArrowDeactivationRadius        = 400.000000                          ### Indicates the radius between entities to start actions
ArrowActiveRadius              = 200.000000                          ### Indicates the radius between entities to start actions
ArrowViewRadius                = 500.000000                          ### Indicates the radius between entities to view the indicator
ArrowTargetFile                = Models/Misc/SMission/SMission       ### This file is the floating arrow.
ArrowMissionFile               = Models/Misc/MMission/MMission       ### This file is the floating arrow.
ArrowUseFile                   = Models/Misc/Action/Action           ### This file is the floating use arrow.
FullCameraTest                 = 0                                   ### Activates/deactivates de camera test.
OutWalkCamFar                  = 400000.000000                       ### default clip far  distance for characters (outdoor)
OutWalkCamNear                 = 20.000000                           ### default clip near distance for characters (outdoor)
WalkCamFar                     = 100000.000000                       ### default clip far  distance for characters (indoor)
WalkCamNear                    = 10.000000                           ### default clip near distance for characters (indoor)
VehicleCamFar                  = 500000.000000                       ### default clip far  distance for vehicles
VehicleCamNear                 = 50.000000                           ### default clip near distance for vehicles
FreeCameraCollide              = 1                                   ### If the camera can collide with the world.
VehicleCamDist2                = 1000.000000                         ### Default camera distance for vehicles in cm
VehicleCamDist                 = 1000.000000                         ### Default camera distance for vehicles in cm
InfernoIDWeap                  = 5                                   ### The default weapon idx for the Inferno
SwarmIDWeap                    = 1                                   ### The default weapon idx for the Swarm
TeslaIDWeap                    = 2                                   ### The default weapon idx for the tesla
ATPCIDWeap                     = 4                                   ### The default weapon idx for the ATPC
DevastatorIDWeap               = 3                                   ### The default weapon idx for the Devastator
VulcanIDWeap                   = 0                                   ### The default weapon idx for the vulcan
LaserIDWeap                    = 6                                   ### The default weapon idx for the laser


HookPlugFunc                   = <Callback function>                 ### HookPlugFunc(VehicleName,state) when the hook changes de state


RestoreUpgradeFunc             = <Callback function>                 ### Function to be called when an upgrade is restored
UseTrafficCollisionSkip        = 1                                   ### 1 if uses 0 if not
STrafficCapsule                = 1500.000000                         ### Small/Minimal Radius of the Traffic Segment
NTrafficCapsule                = 2500.000000                         ### Normal Radius of the Traffic Segment
MNTrafficCapsule               = 2500.000000                         ### Mixed Medium/Normal Radius of the Traffic Segment
HNTrafficCapsule               = 3500.000000                         ### Mixed Heavy/Normal Radius of the Traffic Segment
MTrafficCapsule                = 4000.000000                         ### Medium Radius of the Traffic Segment
HTrafficCapsule                = 6000.000000                         ### Heavy Radius of the Traffic Segment
TrafficSpeed                   = 5600.000000                         ### Terminal speed for the traffic
FXDumbMotorFile                = Models/GFX/DumbMotor.M3D            ### Default Model for Dumb Motor Effect
FXMotorCalimaOffset            = -95.000000                          ### FX Motor Calima Offset
FXMotorCalimaFile              = Models/GFX/MotorCalima.M3D          ### Default Model for Motor Calima Effect
FXMotorCalima                  = 1                                   ### Motor Calima DUDV Deformation Effect
FXMotorSmokeFile               = Models/GFX/MotorSmoke.M3D           ### Default Model for Motor Smoke Effect
FXVehicleDeathTrailFile        = Models/GFX/VehicleDeathTrail.M3D    ### Default Model for Remaining Vehicle Trails after Death
FXEngineGlowSizeAtt            = 0.050000                            ### FX Engine Glow Size Attenuation Factor
FXEngineGlowSizeMax            = 1200.000000                         ### FX Engine Glow Size Maximun
FXEngineGlowSize               = 450.000000                          ### FX Engine Glow Size at Distance
FXEngineGlowDistFadeTo         = 7000.000000                         ### FX Engine Distance to Glow Fade To
FXEngineGlowDistFadeMid        = 6000.000000                         ### FX Engine Distance to Glow Fade Middle
FXEngineGlowDistFadeFrom       = 5000.000000                         ### FX Engine Distance to Glow Fade From
FXEngineGlowDistFadeMult       = 1.000000                            ### FX Engine Distance to Glow Fade Mult
FXEngineTrailOffset            = 450.000000                          ### Offset Z of Engine trail
FXEngineTrailDistSpeedFactor   = 0.028000                            ### Speed Factor for add to Engine Trail Dist
FXEngineTrailDist              = 400.000000                          ### Distance of Engine trail segments at Max Trust
FXEngineTrailHideTime          = 5.000000                            ### Time to Hide the trail of a Hidden Engine
FXEngineTrailSize              = 80.000000                           ### Size of Engine trail
FXEngineBirthRate              = 20                                  ### BirthRate at Trust 0, (always 100 at Max Trust)
EnginePathFmt                  = Models/Vehicles/Engines/%s/%s.m3d    ### The full path of the Vehicle Engines.
PilotViewDist                  = 22000.000000                        ### Maximun Distance for show the Ship Pilot
MotorTrustRotationY            = 0.250000                            ### Rotation Y Speed produced by the motor trust
MotorTrustRotationX            = 0.250000                            ### Rotation X Speed produced by the motor trust
FxBoostTimeDuration            = 2.000000                            ### Time of the boost FX
FxAccVariation                 = 6.000000                            ### Speed of variation of Acceleration FX
FxVelVariation                 = 6.000000                            ### Speed of variation of Velocity FX
FxAngVariation                 = 4.000000                            ### Speed of variation of Angle FX
FxSpeedVariation               = 4.000000                            ### Speed of variation of Speed FX
VehicleCrashMinTime            = 1.000000                            ### Safe Last crash time detector.
VehicleCrashAccHev             = 672000.000000                       ### Beyond this value, is a Heavy crash cm/seg^2
VehicleCrashAccHi              = 504000.000000                       ### Beyond this value, is a serious crash cm/seg^2
VehicleCrashAccMed             = 336000.000000                       ### Beyond this value, is a medium crash cm/seg^2
VehicleCrashAccLo              = 168000.000000                       ### Maximun SpeedChange to detect crash in cm/seg^2
PlayerTeamID                   = 2                                   ### 0:red, 2:green, 4:Killer
PlayerName                     = Unnamed Player                      ### user's nickname
PlayerMaxLife                  = 185                                 ### The max life for the normal ship configuration...
PlayerModel                    = SBoss1                              ### Model resource
PilotModel                     = P_Betty                             ### Player resource
Motor0Model                    = MBOSS1                              ### The first motor kind
Motor1Model                    = MBOSS1                              ### The Second motor kind
Motor2Model                    =                                     ### The Third motor kind
Motor3Model                    =                                     ### The Fourth motor kind
WeaponBayList                  = 0,15,0,0,15,15,1                    ### List of mounted weapons(codified) A bits,B bits....

iHangarShip                    = 3                                   ### The selected hangar ship
HangarShip9                    = SFunc1<-MPOLI1<-<-<-<-1,0,0,0,1,0,1<-45<-0,0,0,0,0,0    ### 9th Hangar ship values
HangarShip8                    = SPoliBoss1<-MPOLI1<-MPOLIBOSS1<-<-<-0,15,0,7,7,6,1<-150<-0,0,0,0,0,0    ### 8th Hangar ship values
HangarShip7                    = SMerc1<-MMERC1<-<-<-<-1,3,1,0,0,3,1<-80<-0,0,0,0,0,0    ### 7th Hangar ship values
HangarShip6                    = SBanker1<-MBANKER1<-<-<-<-3,1,1,3,0,0,1<-80<-0,0,0,0,0,0    ### 6th Hangar ship values
HangarShip5                    = SMayor1<-MMAYOR1<-<-<-<-0,0,3,3,3,1,1<-80<-0,0,0,0,0,0    ### 5th Hangar ship values
HangarShip4                    = SBoss1<-MBOSS1<-MBOSS1<-<-<-0,15,0,0,15,15,1<-185<-0,0,0,0,0,0    ### 4th Hangar ship values
HangarShip3                    = SMerc3<-MMERC3<-MMERC3<-<-<-0,15,7,0,7,0,1<-150<-0,0,0,0,0,0    ### 3rd Hangar ship values
HangarShip2                    = SBankMaster1<-MBANKMASTER1<-MBANKMASTER1<-<-<-15,15,3,15,0,6,1<-150<-0,0,0,0,0,0    ### 2nd Hangar ship values
HangarShip1                    = SArchbishop1<-MARCHBISHOP1<-MARCHBISHOP1<-<-<-3,0,15,0,15,3,1<-150<-0,0,0,0,0,0    ### 1st Hangar ship values
FreeSpaceMagnetCenterZ         = 0.000000                            ### Center of the sphere freespacemagnet
FreeSpaceMagnetCenterY         = 0.000000                            ### Center of the sphere freespacemagnet
FreeSpaceMagnetCenterX         = 0.000000                            ### Center of the sphere freespacemagnet
FreeSpaceMagnetAccel           = 56000.000000                        ### Big   radius for the freespacemagnet
FreeSpaceMagnetHiRadius        = 95000.000000                        ### Big   radius for the freespacemagnet
FreeSpaceMagnetLoRadius        = 90000.000000                        ### Small radius for the freespacemagnet
FreeSpaceMagnet                = 0                                   ### 1 to activate the freespace sphere
VeCharsPathFmt                 = Models/Vehicles/Characters/%s/%s.m3d    ### The full path of the Vehicle Characters.
ShipPathFmt                    = Models/Vehicles/Ships/%s/%s.m3d     ### The full path of the Ships
VehicleEditingMode             = 0                                   ### 1 to set the vehicle entities in editing mode.
FXVehicleFloatingFactor        = 1.000000                            ### Factor of floating Movement of the ship.
NPCSndMotorVolFactor           = 2.000000                            ### Indicates the extra factor for NPC ship motor engines
HiRacerFov                     = 105.000000                          ### Camera Field of view in racing conditions. (terminal velocity)
LoRacerFov                     = 80.000000                           ### Camera Field of view in racing conditions. (stoped)
MotorDownFactor                = 0.250000                            ### When the ship engines are hacked, factor used to replace de real engine values
AmorPieceWeight                = 10.000000                           ### Weight that minds 1 armor value
FXDevastatorFireTime           = 0.220000                            ### Devastator Fire Time
FXDevastatorFireScale          = 1.500000                            ### Devastator Fire Scale
FXVulcanFireTime               = 0.100000                            ### Vulcan Fire Time
FXVulcanFireScale              = 1.300000                            ### Vulcan Fire Scale
WindFXSmokeSizeDiv             = 850.000000                          ### Wind FX Smoke Size Divisor
WindFXSmokeMaxDist             = 3000.000000                         ### Wind FX Smoke Maximun Distance
WindFXSmokeMinVel              = 7000.000000                         ### Wind FX Smoke Minimun Vehicle Speed
WindFXSmokeTimeStep            = 0.025000                            ### Wind FX Smoke Minimun Time Step
WindFxSmoke                    = 1                                   ### Wind FX Smoke
WindFxSmokeFile                = Models/GFX/WindFX.M3D               ### Default Model for WindFX Smoke Effect
FXVehicleFireFile              = Models/GFX/VehicleFire.M3D          ### Default Model for Vehicle Fire Effect
FXVehicleSputnikFile           = Models/GFX/Sputnik/VehicleSputnik.M3D    ### Default Model for Vehicle Sputnik Effects
FXVehicleEMIFile               = Models/GFX/VehicleEMI.M3D           ### Default Model for Vehicle EMI Effect
FXVehicleDamageFile            = Models/GFX/VehicleDamage.M3D        ### Default Model for Vehicle Damage Effect
FXSetOnFireLifePercent         = 25                                  ### Percent of Life to Set On Fire
FXVehicleSpeedTrailFollowFactor = 0.650000                            ### Vehicle Speed Trails follow factor (0...1)
FXVehicleSpeedTrailFadeOutH    = 10000.000000                        ### Fade Off Speed Trails by Horizontal Speed
FXVehicleSpeedTrailSize        = 12.000000                           ### Size of Vehicle Speed Trails segments
FXVehicleSpeedTrailDist        = 200.000000                          ### Distance of Vehicle Speed Trails segments at Max Speed
VehicleAttackModeMaxDist       = 20000.000000                        ### If attack mode in the pad controller is pressed, minimal distance from objective (auto forwards)
VehicleAttackModeMinDist       = 15000.000000                        ### If attack mode in the pad controller is pressed, minimal distance from objective (auto backwards)
VehicleCenterPadBounce         = 0.750000                            ### Vehicle control for pad controllers.
VehicleCenterPadLock           = 0.000000                            ### Vehicle control for pad controllers.
XtrTimeWSwitchNo               = 1.000000                            ### Additonal time to switch the weapon if no ammo when press fire event.
TimeWSwitchNo                  = 2.000000                            ### time to auto switch the weapon if the fire button is pressed when no ammo.

AttackerMarkTime               = 1.000000                            ### Before this time the attacker will be included in second place at the list

TgtRegenerationTime            = 1.000000                            ### After this time, the cycling list will be regenerated
ItemMissRespawnTime            = 20.000000                           ### Time to respawn the Item -> Missile Ammo
ItemMissAdds                   = 200                                 ### Default Increment to the Item -> Missile Ammo
ItemEnerRespawnTime            = 20.000000                           ### Time to respawn the Item -> Energy Ammo
ItemEnerAdds                   = 375                                 ### Default Increment to the Item -> Energy Ammo
ItemPartRespawnTime            = 20.000000                           ### Time to respawn the Item -> Particle Ammo
ItemPartAdds                   = 250                                 ### Default Increment to the Item -> Particle Ammo


OnLifeItemTaken                = <Callback function>                 ### Function to be called when an item is taken
ItemLifeRespawnTime            = 20.000000                           ### Time to respawn the Item -> Life
ItemLifeAdds                   = 50                                  ### Default Increment to the Item -> Life
VulcanHitUseNormal             = 1                                   ### Use the Normal of Hitted point at Vulcan Hit
FXVulcanHitDistance            = 80000.000000                        ### Distance of Vulcan Sparks Effect
VulcanRicSoundAttEnd           = 0.000000                            ### Vulcan puchuing sound att end
VulcanRicSoundAttIni           = 0.000000                            ### Vulcan puchuing sound att ini
VulcanRic2SoundVol             = 0.150000                            ### Third Vulcan puchuing sound volume
VulcanRic2Sound                = VulcanRic2                          ### Third Vulcan puchuing sound name
VulcanRic1SoundVol             = 0.150000                            ### Second Vulcan puchuing sound volume
VulcanRic1Sound                = VulcanRic1                          ### Second Vulcan puchuing sound name
VulcanRic0SoundVol             = 0.150000                            ### First Vulcan puchuing sound volume
VulcanRic0Sound                = VulcanRic0                          ### First Vulcan puchuing sound name
VulcanDamageEasy               = 1                                   ### Vulcan damage per slot (easy Set)
VulcanDamage                   = 2                                   ### Vulcan damage per slot
VulcanDistLimitUPG             = 40000.000000                        ### Distance limit shoots(UPGRADE)
VulcanDistLimit                = 26666.000000                        ### Distance limit shoots
VulcanTimeDelayUPG             = 0.075000                            ### Time between vulcan shoots (UPGRADE)
VulcanTimeDelay                = 0.100000                            ### Time between vulcan shoots
VulcanAmmoCost                 = 0.500000                            ### Cost Per hit at vulcan
VulcanRange                    = 40000.000000                        ### The maximun range that have the vulcan
VulcanHitForce                 = 1000000.000000                      ### The force that have a single vulcan shoot
VulcanHitFile                  = Models/Weapons/Vulcan/Hit.M3D       ### default hit model for the vulcan
VulcanBulletFile               = Models/Weapons/Bullet/Bullet.M3D    ### default bullet model for the vulcan
VulcanIDAmmo                   = 0                                   ### The default weapon idx for the vulcan
FXTeslaRandRadius              = 500.000000                          ### Random Radius that have the Tesla
FXTeslaStepTime                = 0.060000                            ### Time step to change the follow curve for the Tesla
FXTeslaFollowTime              = 0.025000                            ### Time that use the Tesla to follow the curve
FXTeslaFadeOutTime             = 0.100000                            ### Time that use the Tesla to fade out
TeslaDistLimit                 = 20000.000000                        ### Distance limit shoots
TeslaTrackForce                = 20000.000000                        ### Traking force that have a single tesla shoot with upgrade (TN/Seg)
TeslaMinAngRangeUpgPad         = 17.000000                           ### The minimun angle range with upgrade (no hit case at tesla) Pad Controller
TeslaMinAngRangeUpg            = 12.000000                           ### The minimun angle range with upgrade (no hit case at tesla)
TeslaShootFile                 = Models/Weapons/Tesla/Shoot.M3D      ### default shoot model for the Tesla
TeslaUpRangeTime               = 0.250000                            ### Time to the min to the max ang range if not hit (tesla)
TeslaDownRangeTimePad          = 2.000000                            ### Time to the max to the min ang range if not hit (tesla) Pad Controller
TeslaDownRangeTime             = 0.500000                            ### Time to the max to the min ang range if not hit (tesla)
TeslaAmmoCost                  = 0.300000                            ### Cost Per hit at tesla
TeslaMaxAngRangePad            = 40.000000                           ### The maximun angle range (hit case at tesla) Pad Controller
TeslaMaxAngRange               = 25.000000                           ### The maximun angle range (hit case at tesla)
TeslaMinAngRangePad            = 10.000000                           ### The minimun angle range (no hit case at tesla)  Pad Controller
TeslaMinAngRange               = 5.000000                            ### The minimun angle range (no hit case at tesla)
TeslaRange                     = 20000.000000                        ### The maximun range that have the tesla
TeslaHitForce                  = 500000.000000                       ### The force that have a single tesla shoot
TeslaIDAmmo                    = 2                                   ### The default weapon idx for the tesla
SwarmHitSoundAttEnd            = 35000.000000                        ### Swarm Hit sound attenuation end
SwarmHitSoundAttIni            = 0.000000                            ### Swarm Hit sound attenuation ini
SwarmHitSoundVol               = 0.450000                            ### Swarm Hit sound volume
SwarmHitSound                  = SwarmBoom                           ### Swarm Hit sound name
SwarmBeeSoundAttEnd            = 35000.000000                        ### Swarm Bee sound attenuation end
SwarmBeeSoundAttIni            = 0.000000                            ### Swarm Bee sound attenuation ini
SwarmBeeSoundVol               = 0.250000                            ### Swarm Bee Death sound volume
SwarmBeeSound                  = SwarmBang                           ### Swarm Bee Death sound name
SwarmEngineSoundDoppler        = 1.000000                            ### Swarm Engine sound doppler
SwarmEngineSoundAttEnd         = 35000.000000                        ### Swarm Engine sound attenuation end
SwarmEngineSoundAttIni         = 0.000000                            ### Swarm Engine sound attenuation ini
SwarmEngineSoundVol            = 0.350000                            ### Swarm Engine sound volume
SwarmEngineSound               = SwarmEngine                         ### Swarm Engine sound name
SwarmNumber4                   = 4                                   ###  Swarm Number 4 
SwarmNumber3                   = 5                                   ###  Swarm Number 3 
SwarmNumber2                   = 6                                   ###  Swarm Number 2 
SwarmNumber1                   = 7                                   ###  Swarm Number 1 
SwarmAmmoCost4                 = 22                                  ###  Swarm Ammo Cost 4 
SwarmAmmoCost3                 = 18                                  ###  Swarm Ammo Cost 3 
SwarmAmmoCost2                 = 13                                  ###  Swarm Ammo Cost 2 
SwarmAmmoCost1                 = 7                                   ###  Swarm Ammo Cost 1 
SwarmBeeRadius                 = 24.000000                           ### The Radius add per Bee that have the swarm
SwarmMinRadius                 = 250.000000                          ### The Minimun Radius that have the swarm
SwarmDistLimit                 = 40000.000000                        ### Distance limit shoots
SwarmDamage                    = 4                                   ### Damage per mis.
SwarmTimeDelay                 = 1.500000                            ### Time in seconds between the mis. shoots
SwarmRangeUPG                  = 120000.000000                       ### The maximun range that have the swarm
SwarmRange                     = 60000.000000                        ### The maximun range that have the swarm
SwarmHitForce                  = 200.000000                          ### The Hit Force Energy that have the swarm
SwarmTurnSpeedUPG              = 100.000000                          ### The Turn Speed that have the swarm with Upgrade
SwarmTurnSpeed                 = 60.000000                           ### The Turn Speed that have the swarm
SwarmUpTopSpeed                = 4000.000000                         ### The Up Speed (Vehicle) that have the swarm
SwarmBeesSpeed                 = 20000.000000                        ### The Internal Bees Speed that have the swarm
SwarmFastSpeed                 = 40000.000000                        ### The Fast Speed that have the swarm
SwarmNormSpeed                 = 20000.000000                        ### The Formal Speed that have the swarm
SwarmBeeExplosionFile          = Models/Weapons/Swarm/BeeExplosion.M3D    ### Default Model for Swarm Bee Explosion
SwarmExplosionFile             = Models/Weapons/Swarm/Explosion.M3D    ### Default Model for Swarm Explosion
SwarmMissileFile               = Models/Weapons/Swarm/Swarm.M3D      ### Default Model for Swarm Missile
SwarmArmor                     = 2                                   ### The default armor for one swarm missile
SwarmDeathTime                 = 0.500000                            ### The time for bee death that have the swarm
SwarmLifeTime                  = 4.500000                            ### The maximun lifetime that have the swarm
SwarmIDAmmo                    = 1                                   ### The default ammo idx for the swarm
FXSonicRadius                  = 15000.000000                        ### Radius of Sonic Mine Explosion Effect
FXSonicXpldeFile               = Models/Weapons/Sonic/Xplde.M3D      ### default Xplode model for the Sonic
SonicLifeTime                  = 5.000000                            ### Sonic Life Time
SonicRechargeTime              = -0.750000                           ### Sonic Recharge Time
SonicArmor                     = 25                                  ### Sonic Armor
SonicAmmoNeed                  = 2                                   ### Sonic Ammo Need
SonicIDAmmo                    = 1                                   ### Sonic Ammo ID


SetUpSonicFunc                 = <Callback function>                 ### Function to be called to set up the mine properties


CreateSonicFunc                = <Callback function>                 ### Function to be called to create the mine
FXHookSize                     = 40.000000                           ### Size of Hook
FXHookTensor                   = 7.000000                            ### Tensor Power of Hook (0...1)
FXHookFadeTime                 = 0.200000                            ### Time of Hook Release Fade
FXLaserBeamHeight              = 120.000000                          ### The height of the laser beam
FXLaserBeamSize                = 2200.000000                         ### The size of the laser beam
HookAccel                      = 20000.000000                        ### Acceleration when the hook is plugged at the world.
HookRange                      = 20000.000000                        ### The maximun range that have the Hook
HookEMITime                    = 3.000000                            ### Time of electromagetic interference of the Hook
LaserRicSoundVol               = 0.150000                            ### First Laser puchuing sound volume
LaserRicSound                  = LaserRic                            ### First Laser puchuing sound name
LaserMinSpeed                  = 50000.000000                        ### The minimun Speed of the laser shoots
LaserDistLimit                 = 20000.000000                        ### Distance limit shoots
LaserDamage                    = 3                                   ### Damage per shoot
LaserTimeDelay                 = 0.200000                            ### Time in seconds between the laser shoots
LaserAmmoCost                  = 10.000000                           ### Cost Per hit at laser
LaserRange                     = 30000.000000                        ### The maximun range that have the laser
LaserHitForce                  = 1000000.000000                      ### The force that have a single laser shoot
LaserHookSparksFile            = Models/Weapons/Laser/HookSparks.M3D    ### default model for the hook sparks
LaserHookFile                  = Models/Weapons/Laser/Hook.M3D       ### default model for the hook
LaserShootFile                 = Models/Weapons/Laser/Shoot.M3D      ### default shoot model for the laser
LaserHitFile                   = Models/Weapons/Laser/Hit.M3D        ### default hit model for the laser
LaserIDAmmo                    = 3                                   ### The default weapon idx for the laser
FXInfernoExplosionMaxDist      = 400000.000000                       ### Maximun Distance to show the Inferno Explosion Effect
FXInfernoExplosionFadeTime     = 1.000000                            ### Fade Off Time of the Inferno Explosion Effect
FXInfernoExplosionTime         = 2.500000                            ### Life Time of the Inferno Explosion Effect
FXInfernoCoreSize              = 1250.000000                         ### Core Size of the Inferno Explosion Effect
FXInfernoRayInitSizeMax        = 250.000000                          ### Maximun Initial Size of a Ray in the Inferno Explosion Effect
FXInfernoRayInitSizeMin        = 20.000000                           ### Minimun Initial Size of a Ray in the Inferno Explosion Effect
FXInfernoRayAccMax             = 950.000000                          ### Maximun Acceleration of a Ray in the Inferno Explosion Effect
FXInfernoRayAccMin             = 450.000000                          ### Minimun Acceleration of a Ray in the Inferno Explosion Effect
FXInfernoRaySpeedMax           = 19000.000000                        ### Maximun Speed of a Ray in the Inferno Explosion Effect
FXInfernoRaySpeedMin           = 14000.000000                        ### Minimun Speed of a Ray in the Inferno Explosion Effect
FXInfernoRayMinSize            = 150.000000                          ### Min Ray Size of Inferno Explosion Effect
FXInfernoRayRadius             = 0.300000                            ### Ray Radius of Inferno Explosion Effect
InfernoInvUpgExtraDamage       = 0.900000                            ### Inferno Upgrade (inversed extended damage factor)
InfernoUpgFireFactor           = 4.000000                            ### Inferno Upgrade Fire Factor
InfernoUpgFireTime             = 20.000000                           ### Inferno Upgrade Fire Time
InfernoMaxDamage               = 225.000000                          ### Maximun damage of Inferno
InfernoMinDamage               = 5.000000                            ### Minimal damage of Inferno
InfernoHitSoundAttEndRadius    = 3.000000                            ### Inferno Hit sound attenuation end by radius
InfernoHitSoundAttIniRadius    = 0.000000                            ### Inferno Hit sound attenuation ini by radius
InfernoHitSoundVol             = 0.300000                            ### Inferno Hit sound volume
InfernoHitSound                = InfernoBoom                         ### Inferno Hit sound name
InfernoEngineSoundDoppler      = 1.000000                            ### Inferno Engine sound doppler
InfernoEngineSoundAttEnd       = 35000.000000                        ### Inferno Engine sound attenuation end
InfernoEngineSoundAttIni       = 0.000000                            ### Inferno Engine sound attenuation ini
InfernoEngineSoundVol          = 0.320000                            ### Inferno Engine sound volume
InfernoEngineSound             = InfernoEngine                       ### Inferno Engine sound name
InfernoAmmoCost                = 125                                 ### Inferno Ammo Cost
InfernoRangeBay                = 10000.000000                        ### Range add per bay that have the Inferno
InfernoRangeMin                = 10000.000000                        ### Range without bays that have the Inferno
InfernoDistLimit               = 40000.000000                        ### Distance limit shoots
InfernoHitForce                = 75000.000000                        ### The Hit Force Energy that have the Inferno cm*TN/sec
InfernoTimeDelay               = 3.000000                            ### Time in seconds between the mis. shoots
InfernoTurnSpeed               = 20.000000                           ### The Turn Speed that have the Inferno
InfernoUpTopSpeed              = 4000.000000                         ### The Up Speed (Vehicle) that have the Inferno
InfernoBeesSpeed               = 2000.000000                         ### The Internal Bees Speed that have the Inferno
InfernoFastSpeed               = 16000.000000                        ### The Fast Speed that have the Inferno
InfernoNormSpeed               = 12000.000000                        ### The Formal Speed that have the Inferno
InfernoExplosionFile           = Models/Weapons/Inferno/Explosion.M3D    ### Default Model for Inferno Explosion
InfernoMissileFile             = Models/Weapons/Inferno/Inferno.M3D    ### Default Model for Inferno Missile
InfernoArmor                   = 4                                   ### The default armor for one swarm missile
InfernoLifeTime                = 6.500000                            ### The maximun lifetime that have the Inferno
InfernoIDAmmo                  = 1                                   ### The default ammo idx for the Inferno
EMIThunderSoundAttEnd          = 0.000000                            ### EMI thunder sound attenuation end
EMIThunderSoundAttIni          = 0.000000                            ### EMI thunder sound attenuation ini
EMIThunderSoundVol             = 0.100000                            ### EMI thunder sound volume
EMIThunder2Sound               = EMIRayo2                            ### EMI thunder 2 sound name
EMIThunder1Sound               = EMIRayo1                            ### EMI thunder 1 sound name
FXEMIRandRadius                = 850.000000                          ### Random Radius that have the EMI Lighting
FXEMIStepTime                  = 0.040000                            ### Time step to change the follow curve for the EMI Lighting
FXEMIFollowTime                = 0.025000                            ### Time that use the EMI Lighting to follow the curve
EMILowRadiusFactor             = 0.400000                            ### Radius Low Factor that have the EMI
EMIRadius                      = 1500.000000                         ### Radius that have the EMI
EMIFile                        = Models/Weapons/EMI/EMI.M3D          ### Default Model for Electro Magnetic Interference
EMILifeTime                    = 15.000000                           ### EMI Life Time
EMIRechargeTime                = 1.500000                            ### EMI Recharge Time
EMIAmmoNeed                    = 5                                   ### The deault cost ammunition for the EMI
EMIIDAmmo                      = 2                                   ### EMI Ammo ID


SetUpEMIFunc                   = <Callback function>                 ### Function to be called to set up the EMI properties


CreateEMIFunc                  = <Callback function>                 ### Function to be called to create the EMI
FXDevastatorScale              = 1.200000                            ### Scale of Devastator Explosion Effect
FXDevastatorRadius             = 600.000000                          ### Radius of Devastator Explosion Effect
FXDevastatorDistance           = 95000.000000                        ### Distance of Devastator Explosion Effect
DevastatorDistLimit            = 40000.000000                        ### Distance limit shoots
DevastatorExtraDamage          = 5.000000                            ### Aditional damage about the distance
DevastatorMinDamage            = 2.000000                            ### The base of the minimal damage of Devastator
DevastatorRechargeTime         = 0.250000                            ### Time between a single vulcan shoot.
DevastatorHitForce             = 12000.000000                        ### The force that have a single Devastator shoot cm*TN/sec
DevastatorExplosionRadius      = 1500.000000                         ### Explosion radius by a Single Devastator shoot
DevastatorSpreadAngle          = 3.500000                            ### angle of random values used by Devastator
DevastatorAmmoCost             = 1.000000                            ### Cost Per hit at Devastator
DevastatorRange                = 40000.000000                        ### The maximun range that have the Devastator
DevastatorBoomSoundAttEnd      = 30000.000000                        ### Explosion sound attenuation end for devastator
DevastatorBoomSoundAttIni      = 0.000000                            ### Explosion sound attenuation ini for devastator
DevastatorBoomSoundVol         = 0.100000                            ### Explosion sound volume for devastator
DevastatorBoomSound            = DevastatorBoom                      ### Explosion sound for devastator
DevastatorSparksFile           = Models/Weapons/Devastator/Sparks.M3D    ### default sparks model for the Devastator
DevastatorShootFile            = Models/Weapons/Devastator/Shoot.M3D    ### default shoot model for the Devastator
DevastatorHitFile              = Models/Weapons/Devastator/Hit.M3D    ### default hit model for the Devastator
DevastatorBulletFile           = Models/Weapons/Bullet/Bullet.M3D    ### default bullet model for the Devastator
DevastatorIDAmmo               = 0                                   ### The default weapon idx for the Devastator
CloudFile                      = Models/Weapons/Cloud/Cloud.M3D      ### Default Model for Debris Cloud
CloudLifeTime                  = 10.000000                           ### Cloud Life Time
CloudRechargeTime              = -1.500000                           ### Cloud Recharge Time
CloudIDAmmo                    = 0                                   ### Cloud Ammo ID
CloudAmmoNeed                  = 5                                   ### The default cost ammunition for the cloud


SetUpCloudFunc                 = <Callback function>                 ### Function to be called to set up the cloud properties


CreateCloudFunc                = <Callback function>                 ### Function to be called to create the cloud
ATPCShootSize                  = 950.000000                          ### Max Size of the ATPC Shoot
ATPCTrailTime                  = 0.800000                            ### LifeTime of FadeOut Trail Effect for the ATPC
ATPCCapsuleExtendedSoundAttEnd = 0.000000                            ### ATPC capsule Extended sound att end
ATPCCapsuleExtendedSoundAttIni = 0.000000                            ### ATPC capsule Extended sound att ini
ATPCCapsuleExtendedSoundVol    = 0.300000                            ### ATPC capsule extended sound volume
ATPCCapsuleExtendedSound       = ATPCCapsuleExtended                 ### ATPC capsule extended sound name
ATPCCapsuleSoundAttEnd         = 0.000000                            ### ATPC capsule sound att end
ATPCCapsuleSoundAttIni         = 0.000000                            ### ATPC capsule sound att ini
ATPCCapsuleSoundVol            = 0.300000                            ### ATPC capsule sound volume
ATPCCapsuleSound               = ATPCCapsule                         ### ATPC capsule sound name
ATPCHitSoundAttEnd             = 0.000000                            ### First ATPC puchuing att end
ATPCHitSoundAttIni             = 0.000000                            ### First ATPC puchuing att ini
ATPCHitSoundVol                = 0.500000                            ### First ATPC puchuing sound volume
ATPCHitSound                   = ATPCImpact                          ### First ATPC puchuing sound name
ATPCExtraDamage                = 7                                   ### The xplosion damage for ATPC
ATPCMainDamage                 = 18                                  ### The hit damage for ATPC
ATPCCapsuleSoundRadius         = 6000.000000                         ### Radius for the Sound Capsule for ATPC
ATPCExplosionRadius            = 1000.000000                         ### Radius for the capsule hit for ATPC
ATPCConvDist                   = 2000.000000                         ### Convergence distance (and Start event)
ATPCUpgradeDelay               = 1.000000                            ### Recharge time ATPC (with upgrade)
ATPCDelay                      = 2.000000                            ### Recharge time ATPC
ATPCAmmoCost                   = 10.000000                           ### Cost Per hit at ATPC
ATPCRange                      = 100000.000000                       ### The maximun range that have the ATPC
ATPCHitForce                   = 10000.000000                        ### The force that have a single ATPC shoot
ATPCShootFile                  = Models/Weapons/ATPC/Shoot.M3D       ### default shoot model for the ATPC
ATPCIDAmmo                     = 2                                   ### The default weapon idx for the ATPC
SplitScreen                    = 0                                   ### Is split Screen
ShowCredits                    = 0                                   ### Show credits on main menu?
IsSecondMission                = 0                                   ### Is active any secondary mission?
IsMapOutDoor                   = 1                                   ### Is map outdoor?
Max_Rad_Obj                    = 10000.000000                        ### Min radius of the obj scale

GridScaleY                     = 20000.000000                        ### Y Scale of the entity grid cell
GridScaleX                     = 20000.000000                        ### X Scale of the entity grid cell
GridScaleZ                     = 20000.000000                        ### Z Scale of the entity grid cell

XBRumblePadPad                 = 1.000000                            ### [0..1] rumble power of pad.
XBInvertLRVehicle              = 0                                   ### if true, invert the L&R buttons (vehicle)
XBVehicleAsFPS                 = 0                                   ### if true, controlled as FPS (vehicle)
XBVDigitalAsAnalog             = 0                                   ### if true, the cross is digital (vehicle)
XBInvertVehicleYPad            = 1                                   ### Invert Y Axis in pad (vehicle)
XBInvertLRChar                 = 0                                   ### if true, invert the L&R buttons (character)
XBCameraAutoPad                = 1                                   ### if true, the camera automaticaly turns (character)
XBCDigitalAsAnalog             = 0                                   ### if true, the cross is digital (character)
XBInvertCharYPad               = 1                                   ### Invert Y Axis in pad (character)
XBNumControllers               = 0                                   ### number of plugged controllers
XboxCanSave                    = 1                                   ### Can save games.
NumProfiles                    = 3                                   ### Maximun number of profiles.
XboxSaveName6                  =                                     ### Save game isues.
XboxSaveName5                  =                                     ### Save game isues.
XboxSaveName4                  =                                     ### Save game isues.
XboxSaveName3                  =                                     ### Save game isues.
XboxSaveName2                  =                                     ### Save game isues.
XboxSaveName1                  =                                     ### Save game isues.
XboxSaveName0                  =                                     ### Save game isues.
XboxProfileName                =                                     ### the current save game profile name. If '' no savegame file.
XboxSavePath                   =                                     ### the current save game directory. If '' no savegame file.
GameSkill                      = 0                                   ### Game Skill. (0 = Easy,1 = Normal,2 = Hard).

ServerType                     = TeamDM                              ### Type of server game.

ServerMapList                  = ['FZ']                              ### List of maps to play the game.
Fraglimit                      = 20                                  ### Number of frags to win a match...



ChatEvent                      = <Callback function>                 ### ChatEvent(id) only for racer input modes.   The chat key has been pressed.


QChatEvent1                    = <Callback function>                 ### QChatEvent1(id) only for racer input modes. The quick chat message has been pressed.


QChatEvent2                    = <Callback function>                 ### QChatEvent2(id) only for racer input modes. The quick chat message has been pressed.


QChatEvent3                    = <Callback function>                 ### QChatEvent3(id) only for racer input modes. The quick chat message has been pressed.


QChatEvent4                    = <Callback function>                 ### QChatEvent4(id) only for racer input modes. The quick chat message has been pressed.


QChatEvent5                    = <Callback function>                 ### QChatEvent5(id) only for racer input modes. The quick chat message has been pressed.


QChatEvent6                    = <Callback function>                 ### QChatEvent6(id) only for racer input modes. The quick chat message has been pressed.



MainMissionEvent               = <Callback function>                 ### MainMissionEvent(id) <Mission menu> event when input is not in ´menu´ mode.


EscapeEvent                    = <Callback function>                 ### EscapeEvent(id) <MainMenu> event when input is not in ´menu´ mode.
TopLimit                       = 83091.750000                        ### The hi map limit, after the atmosphere
AtmosphereLimit                = 79543.156250                        ### The atmosphere end
Gravity                        = 4900.000000                         ### Global Gravity

PriorityWeapon                 = Laser, Vulcan, Devastator, Tesla, ATPC, Swarm, Inferno    ### The Seventh Weapon

O_Show                         = 0                                   ### Show Object Pool debug info on screen
ElementModelPath               = Models/Elements/                    ### Path for the element list

ShowDummy                      =                                     ### Show dummys in map.

GridUseTopLimit                = 1                                   ### 1 if the grid will be limited by the toplimit gvar (usually used in outdoors)
FXVehicleAcceleratorFile       = Models/GFX/VehicleAccelerator.M3D    ### Default Model for Vehicle Accelerator Effect
ShipExplosionMaxDist           = 250000.000000                       ### Maximun Distance to show the Ship Explosion Effect
FXShipExplosionFile            = Models/GFX/ShipExplosion.M3D        ### Default Model for Ship Explosion
FXSmokeDebrisFile              = Models/GFX/SmokeDebris.M3D          ### Default Model for Smoke Debris Effect
FXFiredDebrisFile              = Models/GFX/FiredDebris.M3D          ### Default Model for Fired Debris Effect
FXFiredEntitySmokeStep         = 1000.000000                         ### Fired Entity Smoke Effect Step
FXVehicleDamageSmokeStep       = 350.000000                          ### Vehicle Damage Smoke Effect Step
FXSceneTheEndBFile             = Models/GFX/Scenes/TheEndB.M3D       ### Default Model for TheEndB Scene Effects
FXSceneEnterMatrixFile         = Models/GFX/Scenes/EnterMatrix.M3D    ### Default Model for EnterMatrix Scene Effects
FXSceneHumanCDFile             = Models/GFX/Scenes/HumanCD.M3D       ### Default Model for HumanCD Scene Effects
FXSceneBeatPickusFile          = Models/GFX/Scenes/BeatPickus.M3D    ### Default Model for BeatPickus Scene Effects
FXSceneYakuzziFile             = Models/GFX/Scenes/Yakuzzi.M3D       ### Default Model for Yakuzzi Scene Effects
FXSceneBillArrives_AFile       = Models/GFX/Scenes/BillArrives_A.M3D    ### Default Model for Bill Arrives A Scene Effects
FXSceneBishopsFile             = Models/GFX/Scenes/Bishops.M3D       ### Default Model for Bishops Scene Effects
FXSceneDecontaminationFile     = Models/GFX/Scenes/Decontamination.M3D    ### Default Model for Decontamination Scene Effects
FXItemBlinkFile                = Models/GFX/ItemBlink.M3D            ### Item Blink FX Model File
FXItemTakeFile                 = Models/GFX/ItemTake.M3D             ### Default Model for Item Take Effect
FXItemFadeFile                 = Models/GFX/ItemFade.M3D             ### Default Model for Item Fade In/Out Effect
FXShipEditBuildFile            = Models/GFX/Sputnik/ShipEditBuild.M3D    ### Default Model for ShipEdit Build Effects
FXElementsMentalControllerDamageFXMaxDist = 5000.000000                         ### Maximun Distance to show the Elements Mental Controller Damage Effect
FXElementsMentalControllerDamageSoundVol = 1.000000                            ### MentalController Damage Lighting sound volume
FXElementsMentalControllerDamageSound = FXChispas                           ### MentalController Damage Lighting sound name
FXElementsMentalControllerMaxDist = 5000.000000                         ### Maximun Distance to show the Elements Mental Controller Effect
FXABFakeLimitQuakeTime         = 0.100000                            ### 
FXABFakeLimitQuakeFactor       = 0.015000                            ### 
FXABFakeLimitSegmentStep       = 0.038000                            ### 
FXABFakeLimitSegmentSize       = 15000.000000                        ### 
FXABFakeLimitRingRotSpeed      = 2.000000                            ### 
FXABFakeLimitDistLighting      = 20000.000000                        ### 
FXABFakeLimitRadius            = 96000.000000                        ### 
FXElementsFireDropSoundAttEnd  = 45000.000000                        ### Element FireDrop sound attenuation end
FXElementsFireDropSoundAttIni  = 0.000000                            ### Element FireDrop sound attenuation ini
FXElementsFireDropSoundVol     = 0.500000                            ### Element FireDrop Sound volume
FXElementsFireDropSound        = FireDrop                            ### Element FireDrop Sound name
FXElementsFireDropRateAtt      = 1.250000                            ### Rate Attenuation Factor by Distance at Elements Fire Drop Effect
FXElementsFireDropMaxDist      = 200000.000000                       ### Maximun Distance to show the Elements Fire Drop Effect
FXCharacterPoliceGearConversionFile = Models/GFX/Gear/Conversion.M3D      ### Default Model for Gear Conversion Effects
FXFunctionarySpecialActionFile = Models/GFX/Functionary/SpecialAction.M3D    ### Default Model for Functionary Special Action Effects
CharacterConversionSoundVol    = 0.600000                            ### Character Conversion Sound Volume
CharacterConversionSound       = DoFlash                             ### Character Conversion Sound Name
FXCharacterConversionFile      = Models/GFX/CharacterConversion.M3D    ### Default Model for Character Conversion Effect
FXCharacterSputnikFile         = Models/GFX/Sputnik/Sputnik.M3D      ### Default Model for Sputnik Effects
CharacterDeathSoundVol         = 1.000000                            ### Character Death Sound volume
CharacterDeathSound            = CharDeath                           ### Character Death Sound name
FXCharacterDeathMinDist        = 1500.000000                         ### Minimun Distance to Camera for Show Character Death Effect
FXCharacterDeathFile           = Models/GFX/CharacterDeath.M3D       ### Default Model for Character Death Effect
FXCharacterConversorFile       = Models/GFX/CharacterConversor.M3D    ### Default Model for Character Conversor Effect
FXCharacterTeleportFile        = Models/GFX/CharacterTeleport.M3D    ### Default Model for Character Teleport Effect
CharacterTeleportSoundVol      = 0.700000                            ### Character Teleport sound volume
CharacterTeleportDownSound     = transporter4                        ### Character Teleport Down sound name
CharacterTeleportUpSound       = transporter3                        ### Character Teleport Up sound name
FXCharacterBlaBliBlaFile       = Models/GFX/CharacterBlaBliBla.M3D    ### Default Model for BlaBliBla Characters Effect
FXCharacterDazedFile           = Models/GFX/CharacterDazed.M3D       ### Default Model for Dazed Characters Effect
FXMoneyTransferFile            = Models/GFX/MoneyTransfer.M3D        ### Default Model for Money Transfer Effects
PCPadDeadZone                  = 0.200000                            ### Dead zone for analog controllers.


Joy4                           = <List of defines>                   ### User Control definition


Joy3                           = <List of defines>                   ### User Control definition


Joy2                           = <List of defines>                   ### User Control definition


Joy1                           = <List of defines>                   ### User Control definition


Mouse                          = <List of defines>                   ### User Control definition
InvertMouse                    = 0                                   ### 0 = Mouse normal... 1 = Mouse inverted.
MouseSensitivityV              = 1.000000                            ### Vertical Mouse Sensitivity
MouseSensitivityH              = 1.000000                            ### Horizontal Mouse Sensitivity


Kb                             = <List of defines>                   ### User Control definition
CheckInactivityTime            = 120.000000                          ### Inactivity time in seconds to launch the Function.


CheckInactivityFunc            = <Callback function>                 ### Inactivity time function to launch.

LogRumble                      = 0                                   ### Log the input and output to the rumble interface.
PathInPackFile                 =                                     ### Used to convert the system to the new pack system...


OnCrazyDealTarget              = <Callback function>                 ### Function to be called when a crazy deal target is reached


OnCrazyDealFinished            = <Callback function>                 ### Function to be called when a taunt is to be launched
LastSaveGameName               = ABIndoor - 07:43:26                 ### Last SaveGame Name
SelectedLanguage               = German                              ### Actual language.

AlwaysFlushLog                 = 1                                   ### Always flush log file (0/1)
debug                          = 3                                   ### 0 = Nothing, 1 = Something, 2 = Everything, 3 = Everything and much more
PythonExecute                  = import _CrashPad                    ### This will run a pyhon command.
isDemo                         = 0                                   ### Retail version
isXbox                         = 0                                   ### true if console case
isXboxDebug                    = 0                                   ### true if can be acessed the debug info.
LoadMsgString                  = Vergiss nicht, dass sich dein Raumschiff automatisch zum Zielobjekt dreht, wenn du die Funktion "Raumschiff blockieren"  benutzt    ### Message that is show while loading
iLoadMsgString                 = 2                                   ### Loading Message Counter

JoinServerOnStartup            = 0                                   ### if 1 automaticaly joins in a server.
DefaultMaxPlayersOnServer      = 10                                  ### Max number of clients conected to a server.

DefaultServerAddress           = 169.254.224.146                     ### Default conection address.
DefaultServerPort              = 28086                               ### Default conection port.



AfterDrawCallback              = <Callback function>                 ### This function will be called after draw and reseted.
DrawNextFrame                  = 1                                   ### If the next frame will be drawed....
ForceReload                    = 0                                   ###  if set to 1, the nex level will be fully reloaded.
DisableSkipSlot                = 0                                   ### Don't skip slots in low framerates (0/1)
Viewer                         = 0                                   ###  0(default) : Normal game,  1 : Init Viewer
iMap                           = Levels/Menu                         ### The first map that will be loaded
ModPathName                    = mods                                ### Modification path name.
ModFileName                    =                                     ### Modification file name.
```