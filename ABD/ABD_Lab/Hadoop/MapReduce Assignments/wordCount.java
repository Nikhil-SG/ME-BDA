public class wordCount {
	
	public static class testWordCountMapper extends Mapper<LongWritable, Text, Text, IntWritable> {
		public void map(LongWritable key, Text value, Context context) throws IOException, InterruptedException {
					String line = value.toString();
					StringTokenizer tokenizer = new StringTokenizer (line);

					while (tokenizer.hasMoreTokens() ) {
						value.set(tokenizer.nextToken() );
						context.write(value, new IntWritable(1));
					}
		}
	}
	
	public static class testWordCountReducer extends Reducer <Text, IntWritable, Text, IntWritable > {
		public void reduce(Text key, Iterable<IntWritable> values, Context context) 
			throws IOException, InterruptedException {
				int sum = 0;
				for (IntWritable x: values) {
					sum += x.get();
				}
				context.write(key, new IntWritable(sum) );
		}
	}

	public static void main(String[] args) throws Exception{
		// TODO Auto-generated method stub
		Configuration conf = new Configuration();
		
		Job job = Job.getInstance(conf, "my count");

		job.setJarByClass(wordCount.class);
		job.setMapperClass(testWordCountMapper.class);
		job.setReducerClass(testWordCountReducer.class);

		job.setOutputKeyClass(Text.class);
		job.setOutputValueClass(IntWritable.class);

		FileInputFormat.addInputPath(job, new Path(args[0]));
		
		FileOutputFormat.setOutputPath(job, new Path(args[1]));

		System.exit(job.waitForCompletion(true) ? 0: 1);
	}

}
