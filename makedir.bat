@echo off
setlocal enableDelayedExpansion
FOR /l %%N in (1,1,94) do (
    set "DIRNAME=Day%%N"
    md !DIRNAME!
)