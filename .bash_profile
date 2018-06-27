function parse_git_branch { 
   git branch --no-color 2> /dev/null | sed -e '/^[^*]/d' -e 's/* \(.*\)/(\1)/' 
} 
export PS1="\[\e[34;0m\][\T]\W: \$(parse_git_branch)\n:>\[\e[0m\]"

