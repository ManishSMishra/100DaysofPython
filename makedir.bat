@echo off
setlocal enableDelayedExpansion
FOR /l %%N in (1,1,100) do (
    set "DIRNAME=Day%%N"
    md !DIRNAME!
)