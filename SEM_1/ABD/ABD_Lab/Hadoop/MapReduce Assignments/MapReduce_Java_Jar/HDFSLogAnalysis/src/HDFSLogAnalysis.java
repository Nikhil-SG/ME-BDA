import java.io.IOException;
import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.Mapper;
import org.apache.hadoop.mapreduce.Reducer;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;

public class HDFSLogAnalysis {

    // Mapper Class
    public static class LogMapper extends Mapper<LongWritable, Text, Text, IntWritable> {
        private final static IntWritable one = new IntWritable(1);

        public void map(LongWritable key, Text value, Context context) throws IOException, InterruptedException {
            String line = value.toString();
            String[] tokens = line.split("\\s+");

            // Ensure there are enough tokens
            if (tokens.length >= 6) {
                String logType = "";

                // Extract log types based on patterns
                if (tokens[4].equals("dfs.DataNode$PacketResponder:")) {
                    logType = "PacketResponder terminating";
                } else if (tokens[4].equals("dfs.FSNamesystem:") && tokens[5].contains("NameSystem.addStoredBlock:")) {
                    logType = "addStoredBlock";
                } else if (tokens[4].equals("dfs.FSDataset:") && tokens[5].equals("Deleting")) {
                    logType = "Block Deletion";
                } else if (tokens[4].equals("dfs.DataNode$DataXceiver:") && tokens[5].equals("Receiving")) {
                    logType = "Block Receiving";
                } else if (tokens[4].equals("dfs.DataBlockScanner:") && tokens[5].equals("Verification") && tokens[6].equals("succeeded")) {
                    logType = "Block Verification Success";
                }

                // Emit log type and count
                if (!logType.isEmpty()) {
                    context.write(new Text(logType), one);
                }
            }
        }
    }

    // Reducer Class
    public static class LogReducer extends Reducer<Text, IntWritable, Text, IntWritable> {
        public void reduce(Text key, Iterable<IntWritable> values, Context context) throws IOException, InterruptedException {
            int sum = 0;

            // Sum counts for each log type
            for (IntWritable val : values) {
                sum += val.get();
            }

            // Output log type and total count
            context.write(key, new IntWritable(sum));
        }
    }

    // Main method
    public static void main(String[] args) throws Exception {
        Configuration conf = new Configuration();
        Job job = Job.getInstance(conf, "HDFS Log Analysis");

        job.setJarByClass(HDFSLogAnalysis.class);
        job.setMapperClass(LogMapper.class);
        job.setReducerClass(LogReducer.class);

        job.setOutputKeyClass(Text.class);
        job.setOutputValueClass(IntWritable.class);

        FileInputFormat.addInputPath(job, new Path(args[0]));
        FileOutputFormat.setOutputPath(job, new Path(args[1]));

        System.exit(job.waitForCompletion(true) ? 0 : 1);
    }
}
