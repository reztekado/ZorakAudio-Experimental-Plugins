# 3D Panner Manager

Scene-wide camera controller for linked Hyperreal 3D Panner instances.

The manager publishes a named scene and camera state over the DSP-JSFX IPC bus. Linked panners keep their own source positions, then render those positions through the shared manager camera.
