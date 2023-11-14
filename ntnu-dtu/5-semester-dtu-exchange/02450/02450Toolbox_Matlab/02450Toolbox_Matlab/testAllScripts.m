cwd=pwd();
if ~strcmp(cwd(end-6:end),'Scripts')
    cd('.\Scripts')
end
scripts = dir(); 
for t=1:length(scripts)
    if scripts(t).name(end)=='m' && ~strcmp(scripts(t).name,'testAllScripts.m') && ~strcmp(scripts(t).name,'ex3_1_3.m') && ~strcmp(scripts(t).name,'ex3_1_4.m') && ~strcmp(scripts(t).name,'ex3_1_5.m')
        disp(['operating on script: ' scripts(t).name]);
        run(scripts(t).name);
        scripts = dir();  % fixes issues in case clear all invoked in a script
    end
end
