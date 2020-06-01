#!/usr/bin/awk -f
BEGIN {pr = 0; re = 0; print "["}
/\<ul\>/ {pr= 1}
/<\/ul>/ {pr = 0}
/References/ {re = 1}
{
	if(pr == 1 && re == 0){	
		if($0 ~ /li class="toclevel-2/ || $0 ~ /li class="toclevel-3/)
		{
			printf "\t{\"origin\": \"%s\", \"name\": \"%s\"},\n", x,substr($4, 8, length($4)-(14));
		}
	}
}
END {print "]"}