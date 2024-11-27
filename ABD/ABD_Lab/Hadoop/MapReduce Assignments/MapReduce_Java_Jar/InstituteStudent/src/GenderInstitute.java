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

public class GenderInstitute {

    public static class GenderMapper extends Mapper<LongWritable, Text, Text, IntWritable> {
        private final static IntWritable boyCount = new IntWritable(1);
        private final static IntWritable girlCount = new IntWritable(1);

        public void map(LongWritable key, Text value, Context context) throws IOException, InterruptedException {
            String line = value.toString();
            String[] tokens = line.split("\\s+");

            // Assuming the first token is the institute name and the fourth token is gender
            if (tokens.length >= 4) {
                String institute = tokens[1];  // First token is the Institute name
                String gender = tokens[3].toLowerCase();  // Fourth token is the Gender

                if (gender.equals("boy")) {
                    context.write(new Text(institute + "_boys"), boyCount);  // Emit institute_boys
                } else if (gender.equals("girl")) {
                    context.write(new Text(institute + "_girls"), girlCount);  // Emit institute_girls
                }
            }
        }
    }

    public static class GenderReducer extends Reducer<Text, IntWritable, Text, IntWritable> {
        public void reduce(Text key, Iterable<IntWritable> values, Context context) throws IOException, InterruptedException {
            int sum = 0;

            // Sum up all the counts for each key (institute_boys or institute_girls)
            for (IntWritable val : values) {
                sum += val.get();
            }
            context.write(key, new IntWritable(sum));  // Output the total count for each key
        }
    }

    public static void main(String[] args) throws Exception {
        // Check for enough arguments
        if (args.length < 2) {
            System.err.println("Usage: GenderInstitute <input path> <output path>");
            System.exit(-1);
        }

        Configuration conf = new Configuration();
        Job job = Job.getInstance(conf, "Gender Count by Institute");
        job.setJarByClass(GenderInstitute.class);
        job.setMapperClass(GenderMapper.class);
        job.setReducerClass(GenderReducer.class);

        job.setOutputKeyClass(Text.class);
        job.setOutputValueClass(IntWritable.class);

        FileInputFormat.addInputPath(job, new Path(args[0]));
        FileOutputFormat.setOutputPath(job, new Path(args[1]));

        System.exit(job.waitForCompletion(true) ? 0 : 1);
    }
}
