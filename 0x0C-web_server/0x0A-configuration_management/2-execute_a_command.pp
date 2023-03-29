#A manifest that kills killmenow process
exec { 'killmenow';
    command => 'pkill killmenow',
} 

