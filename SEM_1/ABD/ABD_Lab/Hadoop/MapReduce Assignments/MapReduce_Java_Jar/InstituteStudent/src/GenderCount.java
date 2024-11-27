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

public class GenderCount {

    // Mapper Class
    public static class GenderMapper extends Mapper<LongWritable, Text, Text, IntWritable> {
        private final static IntWritable one = new IntWritable(1);  // Constant count of 1

        public void map(LongWritable key, Text value, Context context) throws IOException, InterruptedException {
            String line = value.toString();  // Convert line to String
            String[] tokens = line.split("\\s+");  // Split the line by whitespace

            // Ensure the dataset line has the expected number of columns
            if (tokens.length >= 4) {
                String gender = tokens[3];  // The fourth token is the gender (Boy/Girl)
                context.write(new Text(gender), one);  // Emit gender and a count of 1
            }
        }
    }

    // Reducer Class
    public static class GenderReducer extends Reducer<Text, IntWritable, Text, IntWritable> {
        public void reduce(Text key, Iterable<IntWritable> values, Context context) throws IOException, InterruptedException {
            int sum = 0;

            // Sum up all the values for each gender
            for (IntWritable val : values) {
                sum += val.get();
            }
            context.write(key, new IntWritable(sum));  // Output the gender and the total count
        }
    }

    // Main method
    public static void main(String[] args) throws Exception {
        // Check for the right number of arguments
        if (args.length < 2) {
            System.err.println("Usage: GenderCount <input path> <output path>");
            System.exit(-1);
        }

        Configuration conf = new Configuration();
        Job job = Job.getInstance(conf, "Gender Count");

        job.setJarByClass(GenderCount.class);
        job.setMapperClass(GenderMapper.class);
        job.setReducerClass(GenderReducer.class);

        job.setOutputKeyClass(Text.class);
        job.setOutputValueClass(IntWritable.class);

        FileInputFormat.addInputPath(job, new Path(args[0]));
        FileOutputFormat.setOutputPath(job, new Path(args[1]));

        System.exit(job.waitForCompletion(true) ? 0 : 1);
    }

}
