{
  "targets": [
    {
      "target_name": "pg-query",
      "sources": [ "pg-query.cc", "functions.cc" ],
      "include_dirs" : [
 	 			"<!(node -e \"require('nan')\")",
      ],
      "libraries": [ "-lpg_query" ]
    }
  ],
}
