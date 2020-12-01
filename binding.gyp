{
  "targets": [
    {
      "target_name": "pg-query",
      "sources": [ "pg-query.cc", "functions.cc" ],
      "include_dirs" : [
 	 			"<!(node -e \"require('nan')\")",
        "libpg_query/include"
      ],
      "libraries": [ "-L<!(pwd)/libpg_query/linux", "-lpg_query" ]
    }
  ],
}
